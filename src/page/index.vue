<template>
  <div>
    <myHeader></myHeader>
    <div class="article_list">
      <ul>
         <li v-for="i in list">
          <time v-text="i.release_time"></time>
           <!--<img :src=""  >-->
          <router-link :to="'/content/' + i.id">
            {{ i.context }}
          </router-link>
        </li>
      </ul>
    </div>
    <myFooter></myFooter>
  </div>
</template>
<script>
  export default {
    components: { myHeader, myFooter },
    data () {
      return {
        list: []
      }
    },
    created () {
      this.getData()
    },
    methods: {
      getData () {
        this.$api.get('user/index', null, r => {
          this.list = r.data
        })
      }
    }
  }
import myHeader from '../components/header.vue'
import myFooter from '../components/footer.vue'
</script>
<style>
  .article_list {margin: auto;}
</style>
