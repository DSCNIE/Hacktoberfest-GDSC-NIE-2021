<template>
  <div id="app">
    <index />
  </div>
</template>

<script>
import index from "./components/index.vue";

export default {
  name: "App",
  components: {
    index,
  },
};
</script>

<style>
#app {
  padding: 0;
  margin: 0;
}
</style>
