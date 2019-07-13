# WAHH - Chapter 6 - Attacking Authentication

## Authentication

Of all the controls authentication is conceptually the easiest; a user is correctly authenticated, and given access or they are not, and do not get access.
Much like the keys to your home, if someone has a copy they don't need to smash the side window anymore - they can just let themselves in.
For web applications, an attacker, if correctly authenticated will be given access rights up to that users level of trust. 

Authentication is simple in concept but difficult in implementation. Inside many applications lie subtleties ranging from misconfigurations to ill conceived business logic and it has allowed many sites to be compromised.

## Authentication Technologies

The following are some of the authentication technologies developers utilise to defend their applications:

- HTML forms-based
- Multi-factor authentication (MFA)
- Client SSL cert's or smart cards
- HTTP basic and digests authentication schemes
- Windows-integrated authentication using NTLM or Kerberos
- Authentication services (OAuth, etc)

At the time of writing the most common are HTML forms which the user accesses to input their username and password. This is still very prevalent in today's modern web apps. Even banks that use MFA, or on-screen keyboards and so on, still utilise HTML forms during parts of the login process.
HTTP-based schema's such as basic, digest, and windows-integrated methods are used infrequently over the Internet, but may be used commonly within a local Intranet.

This post goes over enumeration and exploitation of common authentication schemes and looks at methods to uncover vulnerabilities.

## Design Flaws in Authentication Mechanisms

Authentication functions are subject more to design implementation errors or flaws in comparison to many of the other security controls. 

__Bad Passwords__

Users cannot be trusted to implement sound password (or pass phrase) controls. Often the users will adopt the easiest password they can remember, and if given the option will only do the minimum necessary in order to gain access to the application. 

During testing, if the application has a sign up or register page it is worth assessing their current password standards. This will aid in any password list construction. Checking sites like [HaveIbeenPwned] is also advisable to search out if users have had their passwords breached in the past - password reuse is very common.

__Hack Steps__

1. Review password rules, if any
2. Self register several accounts with different weak passwords to validate their policy
3. If only one account is allowed - for instance, on bug bounties - then attempt to reset the password several times, each with a new weak password


__Brute-Forcible Logins__

It is always worth checking if the application has any controls in place to prevent brute forcing the login. If an attacker can try unlimited different passwords on the login page without consequence then even a simple script-kiddie can probably pop the application's authentication.

Client-side controls can be implemented to prevent automated or repeated login attempts. Often this is done via JS or by setting up an incrementing cookie such as `failedlogins=1`. Like other client-side controls this has the potential to be bypassed.

A variation on this is by creating a failed login counter within the users session. There will be no indication of this on the client side but all that's needed to overcome this defence is to create fresh sessions during each iteration of the attack by withholding the session cookie in the request.

__Hack Steps__

1. Manually submit several bad login attempts for an account you control, monitoring the error messages you receive.
2. After about 10 failed logins, if the application has not returned a message about account lockout, attempt to log in correctly - if successful there is likely no account lockout policy.
3. If locked out, repeat the steps with a new account and if the application issues any cookies, use a single cookie for each login attempt.
4. Also, if the account is locked out, try entering the correct password to see if it still accepts correct passwords. If so, you can continue a password-guessing attempt even whilst locked out.
5. If you cannot or do not have user access, attempt to enumerate a valid username and make several bad login attempts with this user, looking for the servers response to the bad attempts.
6. Prior to mounting a brute-force on the application, attempt to identify the differences between a failed and successful login. You can use this to discriminate between success and failure during the attack
7. Obtain a list of common username and passwords to rule out superfluous attempts
8. Automate the process of generating login requests using these lists. Monitor the responses to identify any successful responses.
9. If you are attempting several users at once, spread out the attack by using a breadth-first approach rather than depth-first. Two reasons; it gives time between attacking each username which might allay the server defence mechanisms and, you discover common passwords more quickly.

## Verbose Failed Messages

A typical login form requires two pieces of information; account name (usually username or email) and password.
When the login fails you can infer at least one of the credentials was wrong. Some applications may identify which piece of information is wrong such as `no email address found` etc. 

Whilst usernames are not a secret, they are a vital piece needed in order to break through authentication schemes and their enumeration is important. One place where they are often identifiable is in registration forms where it will often say that `userX` is already registered. Additionally, password reset and forgotten password pages are often exploitable by their very nature.

As a general rule, applications with more robust sign ups or which require more than a typical username can often be exploited during the sign up phase by testing the duplication checking mechanism of the application.

This vulnerability may be much more subtle that described above. Error messages as they appear to the user may be identical but the source code or header information may offer additional clues. Using Burp suites comparer tool can allow attackers to compare responses, highlighting any differences.

__Hack Steps__

1. If you know one username already (like an account you have created), submit one login using this username and an incorrect password, and another with a random username.
2. Record the details of the servers response from each request, including the status code, any redirects, information displayed on-screen, and any differences hidden in the HTML page source. Use a proxy to maintain a full history of all traffic to and from the server.
3. Attempt to discover any obvious or subtle differences in the server's responses between the two login attempts.
4. If this fails, repeat for each location where a username can be submitted.
5. If you can identify the difference between valid and invalid usernames from the responses, create a list of common usernames. Automate sending this list of usernames to the server, logging all correct responses.
6. If the application has a account lockout defence, design your brute forcer to use common passwords during the attack in order to increase the change of compromising any account during username enumeration. Burp has a "battering ram" script that will automate sending the username as the password during enumeration.

Another method is to assess the time taken for the application to response between valid and invalid attempts. For instance, if the correct username is identified it may reach back and do a table lookout which will consume resources thus take longer than a simple deny. Also known as a side-channel attack.

It is also worth checking the applications source code. Developers often leave comments and may have forgotten to strip out identifying information which can be used to attack the authentication mechanism.

## Vulnerable Transmission of Credentials

Submission of credentials over HTTP is sure-fire way to getting your accounts popped. Many applications and browsers are aware of this and either block it or let the user know its potentially unsafe.

HTTPS can still leak credentials if its application handling or implementation is flawed, such as:

- Sending credentials via query string parameters during a `POST` request, instead of in the body. This could be logged in the users browser history, web server logs, and any proxy server logs that sit between the service and server.
- Applications which elect to redirect login requests to a different URL often send data using query strings, instead of another HTML form `POST`.
- Using cookies to store credentials, making the session open to replay attacks.

__Hack Steps__

1. Carry out a successful login whilst monitoring all traffic in both directions.
2. ID every situation where the credentials are transmitted in either direction - using your proxy it may be possible to intercept requests/responses containing certain strings.
3. If credentials are submitted in a URL or as a cookie, or submitted from server to client analyse what the developers are trying to achieve. This may lead to exploitation in logic or design flaws in the application.
4. If any credentials are sent in the clear - move to intercept
5. If no credentials are seen to be sent at all - pay close attention to the data being sent. If is is encoded or obfuscated, its likely where the developers are attempting the hide this sensitive information.
6. If credentials are sent via HTTPS but the login page is HTTP, the application may be vulnerable to a MITM.

## Password Change Functionality

Good applications will provide its users with a password change option. However, this feature is often exploitable by an attacker in the following ways:

- They often provide verbose feedback on whether or not a username exists on the platform.
- Likely has no limit on number of guesses against "existing password" field.
- By checking whether the "new password" and "confirm new password" have the same value only after validating the existing password, providing the attacker the current password.

Password change functions are actually rather complex. The application has to make many decisions such as identifying the user, validating existing credentials, integrating with security controls, comparing the new password against the old one and any policies, and returning feedback to the user. There maybe be subtle logic flaws contained within.

__Hack Steps__

1. Identify any password change function within the application. Some applications attempt to obfuscate such functions by not making them publicly facing - thorough recon should find them.
2. Make requests to the function with invalid usernames, passwords, and mismatched "new password" and "confirm new password" values.
3. Try to identify any behaviour that can be used for username enumeration.

Some password reset forms are accessible only by authenticated users and may be missing a username field. Always check for hidden fields which may contain the username. Otherwise attempt to send a username parameter with the request same as you would with the main login form.

## Forgotten Password Functionality

Forgotten password functions often present the user with secondary challenges in place of the main login. This challenge is often easier to guess than the users password. Questions like mother's maiden name, favourite colour, pet dog's name etc are if answered truthfully quite easy to guess given some research into your target. They could also be distilled into a more targeted wordlist for a dictionary attack.

- Sometimes users are given the option to create their own questions. Often, this provides a great vector for attack as users generally create very simple questions, and answers.
- Applications sometimes may relax their number of attempts before being locked out during the reset, or not even implement such a control at all.
- In circumstances where the user has the option to declare a "hint", they often make these incredibly obvious under the false assumption that only they will see it.
- Where an application offers to send a reset link to an email account but does not display the email, check the request for hidden form fields which may list it. This gives the attacker two opportunities, one to identify the users email and to also send the request to an account they own.

__Hack Steps__

1. Identify any forgotten password functionality on the application. 
2. Understand how this works by first testing an account in which you own.
3. If the mechanism uses a challenge, see if the user can set their own challenge and response - this could be used to brute-force using a wordlist.
4. If their is a "hint" in use, the same as above
5. Try to identify any behaviour in the functionality that could be exploited using a brute-forcer or dictionary attack
6. If there is a automatically generated e-mail that is sent after resetting the password, obtain a number of these to see if any patterns are in use - if so, exploit it

## "Remember Me" Functionality

This function allows users to remain logged in even after leaving the web page, or even persisting after closing the browser. Often, this can be an avenue of attack that leads to exploitation of the application.

Some are implemented by a persistent cookie, such as `RememberUser=archibald`. This cookie is trusted by the application which it then uses to authenticate the user, and creates its session bypassing the login. 

Other "remember me" functions set a cookie that contains a persistent session identifier, such as `RememberUser=2415`. When presented with this cookie the application does a lookup in its table and if it matches, authenticates and logins in that user. Like normal tokens, if the session identifiers of other users can be predicted or extrapolated, an attacker can iterate over large number of identifiers. 

__Hack Steps__

1. Activate any "remember me" functionality, and determine whether the function actually works as intended, or if it still requires a user to re-enter their password. 
2. Inspect all persistent cookies, and any other data stored in local storage for identifiers.
3. Even if found data appears to be encrypted or obfuscated, review it critically. Compare the results of several similar usernames for patterns or consistencies.
4. Attempt to modify the contents of the persistent cookie to try to convince the application that another user has saved his details on your computer.

## User Impersonation Functionality

Some applications allow authenticated users to masquerade as other users in order to access data and carry out functions on their behalf. Help desk operators may verbally authenticate with users over the phone and then take over the machine to assist in the users inquiry.

This presents the following design flaws:

- It may be implemented as a "hidden" function, which may not have the proper access controls in place.
- If an administrators account can be impersonated it may allow vertical privilege escalation that results in complete compromise.
- Sometimes this impersonation can be instigated from a login page whereby a "backdoor" password exists. 

__Hack Steps__

1. Identify any impersonation functionality within the application. 
2. Attempt to use the impersonation functionality directly to impersonate other users.
3. Attempt to manipulate any user-supplied data that is processed here in an attempt to impersonate other users.
4. If this works, seek to impersonate any other accounts you have access to.
5. During your brute-forcing attack see if any username have hits on more than one accepted password - this may indicate a "backdoor" to further controls. Pay attention to "logged in as *x*" when attempting to login in as another user.

## Incomplete Validation of Credentials

A good authentication mechanism will enforce controls such as a mix of alphanumeric characters and special characters, minimum length passwords or a combination of both. Further, good applications will validate the password for compliance with these security measures. Not all applications do this; truncating passwords, case-insensitive checks and stripping unusual characters are some ways that validation can be "cheated" by applications, and exploited by attackers. If identified this can decrease the pool of potential passwords guessed in a brute-force.

__Hack Steps__

1. Using an account you control, attempt to login with passwords that are subtly different to the one you setup in accordance with the password schema. Starting off by removing the last character, changing password case, removing special characters and removing JS client side validators. If successful continue experimenting to see how wide spread this exploit runs.
2. Amend your automated password-guessing attacks removing any passwords that meet the new threshold.


## Non-Unique Usernames

Most applications will enforce that users have unique usernames, but every now and again some will not. This is a design flaw:

- If usernames are not unique, it is therefore possible that two identical usernames could also share a common password. This could lead to either rejection by the application **or** bleeding across both users.
- Therefore, an attacker once identifying a username in existence could create many instances of it and use these as test beds for password guessing. 

## Predictable Initial Passwords

In some applications, users are created in batches, or created with an initial password that must be changed on the first login. If this password is very generic, or worse case the same for each new user entered into the database an attacker that is able to spoof or create a new user account may be able to use this as a foothold into the network.

## Insecure Distribution of Credentials

Many applications use a process whereby usernames and/or passwords are sent to the new registrant out-of-band (post, SMS etc). In certain cases this can prove very insecure; issuance of both username and password, failure to ensure change of password on first login and no time limit on first login are all bad practices.
In some cases a URL for activating the account will be sent instead, if this URL is sequential or guessable an attacker may infer the next URL and visit it prior to the new registrant thereby masquerading as a legitimate user.

__Hack Steps__

1. Obtain a new account. If you are not required to set a username or password ascertain how this information is passed on to the new applicant.
2. If a URL activation link is sent, attempt to create several new accounts in quick succession and look for patterns in the URL.
3. Test to see if the activation URL can be accessed multiple times. If not, lock out the target account before reusing the URL to see if this makes it work.



## Fail-Open Login Mechanisms

Flaws in the implementation of authentication go past mere design flaws and are much harder to detect but are often highly insecure. Fail-open login is one particular case of such.

This type of exploit exposes a logic flaw in the application. An example of such might be a **java** null pointer exception that gets raised when no username or password is entered in the request, but allows a successful login. Although in this case no user session would be employed it may still give an attacker access to the inner workings of the application.
This example should not be encountered as even a cursory review of security within the app should mitigate it, but it provides context for how a logic flaw can lead to a *Fail-Open*.

__Hack Steps__

1. Perform a complete login with an account you own and record every piece of data submitted to the application, and every response received.
2. Repeat this login numerous times, modifying the submitted data in unexpected ways each time. E.g:
  - submit an empty string as the value
  - remove name/value pair together
  - submit very long and very short values
  - submit strings for integers and visa versa
  - submit the same item multiple times, with the same and different values
3. For each malformed request submitted, review the applications response closely for any divergences from the base case.
4. Feed these observations back into framing your test case. When one change alters behaviour try adding this with some other piece of data to see the results

## Defects in Multistage Login

Some applications have multistage logins that may require the user to input some other form of identifier. Such steps may include entering a PIN, a challenge/ response word or anything to can enhance security. It is in the transitions between theses stages that exploits lie. 

For instance:

- An application may assume that in order to reach 'stage three' the user must have successfully authenticated through steps one and two. Therefore, an attacker that jumps from stage one to three may bypass two and allow a login that otherwise was not intended.
- Applications may trust the data received in the latter stages, again thinking that it passed the validations previously. Attackers may be able to send malicious data in latter steps that otherwise would not be permissible in earlier stages.
- The application may also assume that the same user is authenticating through all the steps sequentially. For instance, stage one may require submission of username and password and step two might require the password to be resubmitted. However, the username is also resubmitted but this time in a hidden HTML field. 

__Hack Steps__

1. Perform a complete, valid login using an account you control. Record all data submitted using a proxy.
2. Identify each distinct stage of the login and data that is collected at each stage. Determine whether any single piece of information is collected more that once or is ever transmitted to the client and resubmitted via a hidden form field, cookie, or preset URL parameter.
3. Repeat the login numerous time with fuzzed data:
  - login in different sequence
  - start at any step other than intended
  - try skipping each step then continuing
4. If any data is submitted more than once, try submitting a different value at different stages, and see whether the login is still successful. Sometimes, extra submissions are superfluous and not validated, or that data validated at one point is trusted sequentially through the process.
5. Pay attention to any data being sent by the client that is not entered directly by the user. This may indicate data that is used to indicate the state of the login process, and it may be an avenue of exploitation.

## Insecure Storage of Credentials

If the login credentials are stored insecurely this can circumvent otherwise perfect authentication security controls. An example of this is a database that contains passwords in plain text.  Likewise, insufficient or insecure hashing of passwords may expose passwords to precomputed rainbow table attacks.

## Securing Against Auth Attacks

Many of the exploits listed have _best practice_ mitigations. How password resets should be architectured, secure generation of username and passwords, brute-force preventative measures, and secure account recovery steps. Its an exhaustive list, but worthy of its own document. 

One particularly import piece of authentication is logging, monitoring and notification. It is listed as number ten in the [OWASP top 10].

Some guidelines:
- All login and access control events should be logged; login, logout, password change and reset, and account suspension and recovery. 
- Failed and successful logins should be logged with IP address and username. No passwords or sensitive data should be logged as this presents a opportunity for data spillage.
- All anomalies in authentication events should be sent to real-time monitoring systems. For example, brute-forcing events should be detected and administrators alerted.
- Users must be notified out-if-band when security events occur against their account, such as password changes.
- After a successful login, users should be presented with information about their last login, and the number of unsuccessful login attempts.
- Logging should be generated in a format that can be consumed by various other logging and analysis solutions.

## Closing

Authentication allows an previously unprivileged user to access levels up to the level of the account in which they are able to login into. And, if they have or are able to gain those credentials without arising much suspicion have effectively negated the need to attack the application in ways which may have unintended consequences or lead to creased security posture.

This makes it exploiting any vulnerabilities a valuable proposition for would be attackers. And, the design and implementation problems found in many applications make this defence weaker and more appealing then developers and blue teamers would like. 

To make matters worse, users themselves can't be trusted. They will often use weak credentials, hints or allow other vectors to be used against them, such as password and username reuse.

For the attacker, all it takes is a meticulous and thorough search - look everywhere. Every corner of the application that has a form of authentication should be examined closely and referenced against all the information already gleaned. Scrutiny is your friend, and time spent in reconnaissance is seldom wasted.

[OWASP top 10]: https://www.owasp.org/index.php/Top_10-2017_A10-Insufficient_Logging%26Monitoring
[HaveIbeenPwned]: https://haveibeenpwned.com
