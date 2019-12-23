const name = "hon"
const age = 44

const hi = `my name is ${name} and i am ${age} years old`

console.log(hi)

const s = 'he workd'

var t = hi.split(' ')
console.log(t)

const numbers = new Array(1, 2, 3, 4, 5); // array constructor
const fruits = ['apples', 'bananas', 'jackfruit']
console.log(`${numbers[2]} ${fruits}`)
fruits.push('grapes')
console.log(`${numbers[2]} ${fruits}`)
fruits.unshift('strawberries')
console.log(`${numbers[2]} ${fruits}`)
fruits.pop();
console.log(`${numbers[2]} ${fruits}`)

console.log(fruits.indexOf('apples'))

const person = {
    firstName: 'jj',
    lastName: 'smiath',
    age: 40,
    hobbies: ['music', 'sports', 'reading'],
    address: {
        street: '123 fake st',
        city: 'oaklahoma',
        state: 'WA'
    }
}

console.log(person)
console.log(person.firstName)
console.log(person.age)
console.log(person.hobbies[0])
console.log(person.address.city)

const { firstName, lastName, address: { street} } = person;
console.log(lastName, street)

person.email = `${firstName}.${lastName}@email.com`
console.log(person.email)
