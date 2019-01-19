<template>
  <div>
    <van-tabbar  v-model="active"  active-color="#07c160" @change="test()">
    <van-tabbar-item icon="home-o" >
      <router-link to="/">首页</router-link>
    </van-tabbar-item>
    <van-tabbar-item icon="setting-o">
      <router-link to="user">我的</router-link>
    </van-tabbar-item>
  </van-tabbar>
  </div>
</template>
<script>

export default {
  methods:{
      test:function () {

      }
  },
  data() {
      return {
        active: 0
      }
    }
}

</script>
