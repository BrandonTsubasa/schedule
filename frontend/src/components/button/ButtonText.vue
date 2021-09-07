<template>
  <div id="ButtonText">
    <v-btn class="font-weight-bold primary lighten-1 float-right">
      {{ message }}
    </v-btn>
  </div>
</template>

<script>
export default {
  name: "userEdit",
  data: () => ({}),
  methods: {},
  props: {
    message: {
      type: String,
      default: "",
    },
  },
};
</script>

<style>
#ButtonText {
  width: 100%;
  height: 100%;
}
</style>
