<template>
  <v-app>
    <header>
      <v-app-bar app dark>
        <v-app-bar-nav-icon @click="drawer = true"></v-app-bar-nav-icon>
        <v-toolbar-title>{{ words.app.title }}</v-toolbar-title>
        <v-spacer></v-spacer>
        <p>
          {{ words.app.login }}<span class="font-weight-bold"> {{ loginUser }}</span>
        </p>
      </v-app-bar>
      <v-navigation-drawer v-model="drawer" fixed temporary>
        <v-list-item-group>
          <v-list-item @click="signUpSwitch" v-if="showFlag">
            <v-list-title>{{ words.app.signUp }}</v-list-title>
          </v-list-item>
          <v-list-item @click="signInSwitch" v-if="showFlag">
            <v-list-title>{{ words.app.signIn }}</v-list-title>
          </v-list-item>
          <v-list-item @click="UserSwitch">
            <v-list-title>{{ words.app.user }}</v-list-title>
          </v-list-item>
          <v-list-item @click="Logout">
            <v-list-title>{{ words.app.logout }}</v-list-title>
          </v-list-item>
        </v-list-item-group>
      </v-navigation-drawer>
    </header>
    <v-main class="mt-5">
      <div class="page-switch">
        <v-btn
          class="text-capitalize caption font-weight-bold"
          height="48px"
          color="grey darken-1"
          outlined
          style="border-color: #979797"
          tile
          x-large
          @click="taskSwitch"
        >
          {{ words.app.task }}
        </v-btn>

        <v-btn
          class="text-capitalize caption font-weight-bold"
          height="48px"
          color="grey darken-1"
          outlined
          style="border-color: #979797"
          tile
          x-large
          @click="calSwitch"
        >
          {{ words.app.calendar }}
        </v-btn>
      </div>
    </v-main>

    <router-view></router-view>
  </v-app>
</template>

<script>
import totalApis from "@/common/totalApis.js";
import totalPages from "@/common/totalPages.js";
import words from "@/words/words.json";
import axios from "axios";

export default {
  name: "app",
  data: () => ({
    words: words,
    drawer: false,
    loginUser: null,
    result: null,
    showFlag: true,
  }),

  methods: {
    taskSwitch: function () {
      this.$router.push(totalPages.pages().Task);
    },
    calSwitch: function () {
      this.$router.push(totalPages.pages().TaskCalendar);
    },
    signUpSwitch: function () {
      this.$router.push(totalPages.menuPages().SignUp);
    },
    signInSwitch: function () {
      this.$router.push(totalPages.menuPages().SignIn);
    },
    UserSwitch: function () {
      this.$router.push(totalPages.menuPages().User);
    },
    Logout: function () {
      if (localStorage.getItem("userName").includes("ゲストユーザー")) {
        let userId = localStorage.getItem("userId");
        axios({
          method: "delete",
          url: `${totalApis.apis().userDelete + userId}/`,
          headers: {
            Authorization: `JWT ${localStorage.getItem("JWT")}`,
          },
        })
          .then((response) => {
            console.log(response);
            localStorage.clear();
            this.loginUser = null;
            this.$router.push(totalPages.menuPages().SignIn);
          })
          .catch((error) => {
            console.log(error);
          });
      } else {
        localStorage.clear();
        this.loginUser = null;
        this.$router.push(totalPages.menuPages().SignIn);
      }
    },
  },
  beforeUpdate: function () {
    if (!localStorage.getItem("userName")) {
      this.showFlag = true;
    } else {
      this.showFlag = false;
      this.loginUser = localStorage.getItem("userName");
    }
  },
};
</script>

<style scoped>
#app {
  width: 100%;
  height: 100%;
  background-color: #cccccc;
}
.page-switch {
  text-align: center;
}
</style>
