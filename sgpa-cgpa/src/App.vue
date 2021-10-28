<template>
  <div id="app">
    <h1
      class="heading is-size-3 has-text-centered is-underlined has-text-weight-bold is-family-monospace"
    >
      SGPA-CGPA CALCULATOR
    </h1>
    <div class="box mt-6 tabs is-toggle is-toggle-rounded is-centered">
      <ul>
        <li @click="show = false" :class="{ 'is-active': !show }">
          <a>
            <span class="icon is-small"
              ><i class="fas fa-graduation-cap"></i
            ></span>
            <span>SGPA</span>
          </a>
        </li>
        <li @click="show = true" :class="{ 'is-active': show }">
          <a>
            <span class="icon is-small"
              ><i class="fas fa-graduation-cap"></i
            ></span>
            <span>CGPA</span>
          </a>
        </li>
      </ul>
    </div>
    <sgpa v-if="!show"/>
    <cgpa v-else/>
  </div>
</template>

<script>
import cgpa from './components/cgpa.vue'
import sgpa from './components/sgpa.vue'

export default {
  name: 'App',
  components: {
    cgpa,
    sgpa,
  },
  data(){
    return{
       show: false,
    }
  }
}
</script>

<style>
#app{
  background-color:rgb(243, 241, 234);
  padding-left:10vh;
   padding-right:10vh;
}
.box{
  background-color: inherit;
}
</style>
