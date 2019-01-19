<template>
  <div>
    <van-tabbar  v-model="active"  active-color="#07c160" @change="test()">
    <van-tabbar-item icon="home-o" >首页</van-tabbar-item>
    <van-tabbar-item icon="search">标签</van-tabbar-item>
    <van-tabbar-item icon="setting-o">我的</van-tabbar-item>
  </van-tabbar>
  </div>
</template>
<script>

export default {
  methods:{
      test:function () {
         alert(123)
      }
  },
  data() {
      return {
        active: 0
      }
    }
}

</script>
