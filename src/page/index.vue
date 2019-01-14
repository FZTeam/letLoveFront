<template>
  <div>index</div>
</template>
<script>
export default {
  created () {
//    this.$api.get('topics', null, r => {
    this.$api.get('user/hello', null, r => {
      alert(r)
    })
//    this.$api.get('topics', null, r => {
//      console.log(r)
//    })
  }
}
</script>
