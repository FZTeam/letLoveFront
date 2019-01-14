<template>
   <div id="testApi">
  </div>
</template>
<body>
<div id="testApi1">
     <h1>{{ info }}</h1>
  </div>
<script>
import Vue from 'vue'
const axios = require('axios');
var  data;
export default {
  name: 'TestApi',
  data () {
    return {
      author: "there is nonthing",
      users:[]
    }
  },
  mounted () {
    axios
      .get('https://api.coindesk.com/v1/bpi/currentprice.json')
      .then(response => (data= response))
  }
}
new Vue({
  el: '#testApi1',
  data: {
    info: data
  }
})
</script>
</body>
