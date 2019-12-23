const request= require('request')


request('https://jsonplaceholder.typicode.com/todos/1', {json: true}, (err,res,body) => {
    if (err) {return console.log(err);}
    console.log(body);
    console.log(body.title);
});