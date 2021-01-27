let data = []
const axios = require('axios')
const apiUrl = 'http://localhost:1337'
axios.get(apiUrl + '/meteos').then((response) => {
let resdata = response.data
for (let i = 0; i < resdata.length; i++) {
    let row = resdata[i]
    data.push({
    date: new Date(row.published_at),
    name: 'temperature' + i,
    value: parseInt(row.Batch[5].b.split(' °')[0])
    })
}
})
document.write(data);