<template>
  <div>
    <myHeader></myHeader>
    <van-list  v-model="loading"  :finished="finished"  finished-text="没有更多了"  @load="getData">
      <van-cell    v-for="(confess,index) in confesslist"    :key="confess.index"     >
        <br>
        <time v-text="confess.release_time"></time>
        <router-link :to="'/content/' + confess.id">
          {{ confess.context }}
        </router-link><br/>
      </van-cell>
    </van-list>
    <myFooter></myFooter>
  </div>
</template>
<script>
export default {
    components: { myHeader, myFooter },
    data () {
      return {
        confesslist: [],
        loading: false,
        finished: false
      }
    },
    created () {
      this.getData()
    },
    methods: {
      getData () {
         // 异步更新数据
       this.$api.get('user/index', null, r => {
          this.confesslist = r.data
            // 加载状态结束
        this.loading = false;
         // 数据全部加载完成
        this.finished = true;
        })

      }

    }
}
import myHeader from '../components/header.vue'
import myFooter from '../components/footer.vue'
</script>
