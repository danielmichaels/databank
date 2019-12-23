var axios = require('axios')

axios.all([
    axios.get('https://jsonplaceholder.typicode.com/todos/1'),
    axios.get('https://httpbin.org/json')
]).then(axios.spread((resp1, resp2)=>{
    console.log(resp1.data)
    console.log(resp2.data)
})).catch(error => {
    console.log(error)
});