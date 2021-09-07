<template>
  <div id="User">
    <v-container class="mt-5">
      <h3>{{ words.user.title }}</h3>
      <v-row class="mt-5">
        <v-col cols="4">
          <div @click="editUserName">
            <ButtonText :message="words.user.userName"></ButtonText>
          </div>
        </v-col>

        <v-col cols="4">
          <div @click="editUserEmail">
            <ButtonText :message="words.user.mail"></ButtonText>
          </div>
        </v-col>

        <v-col cols="4">
          <div @click="editUserPassword">
            <ButtonText :message="words.user.password"></ButtonText>
          </div>
        </v-col>
      </v-row>
    </v-container>

    <v-divider></v-divider>

    <v-container>
      <v-row>
        <v-col>
          <v-card class="py-5">
            <v-card-title class="font-weight-bold">
              <h3>{{ words.user.userList }}</h3>
              <v-spacer></v-spacer>
              <v-text-field
                v-model="search"
                append-icon="mdi-magnify"
                :label="words.user.search"
                single-line
                hide-detail
              ></v-text-field>
            </v-card-title>
            <v-data-table
              :headers="headers"
              :items="userDatas"
              :search="search"
              locale="ja"
            >
              <template v-slot:[`item.delete`]="{ item }">
                <v-btn
                  small
                  class="red lighten-1 font-weight-bold white--text"
                  @click="dialogDelete(item)"
                >
                  {{ words.user.delete }}
                </v-btn>
                <v-dialog v-model="confirm" max-width="500px">
                  <v-card>
                    <v-card-title> {{ words.user.confirm }} </v-card-title>
                    <v-card-actions>
                      <v-spacer></v-spacer>
                      <v-btn @click="close">{{ words.user.close }}</v-btn>
                      <v-btn @click="deleteConfirm" class="red lighten-1 white--text">{{
                        words.user.delete
                      }}</v-btn>
                    </v-card-actions>
                  </v-card>
                </v-dialog>
              </template>
            </v-data-table>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>
<script>
import axios from "axios";
import totalApis from "@/common/totalApis.js";
import totalPages from "@/common/totalPages.js";
import ButtonText from "@/components/button/ButtonText.vue";
import words from "@/words/words.json";

export default {
  name: "User",
  data: () => ({
    words: words,
    search: "",
    userDatas: [],
    selectedUser: [],
    headers: [
      { text: "ユーザー名", value: "name" },
      { text: "メールアドレス", value: "email" },
      { text: "削除", value: "delete", sortable: false },
    ],
    confirm: false,
    loginUser: null,
  }),
  components: {
    ButtonText,
  },
  methods: {
    editUserName: function () {
      this.$router.push(totalPages.userSettings().UserNameEdit);
    },
    editUserEmail: function () {
      this.$router.push(totalPages.userSettings().UserEmailEdit);
    },
    editUserPassword: function () {
      this.$router.push(totalPages.userSettings().UserPasswordEdit);
    },
    getUsers: function () {
      axios({
        method: "get",
        url: totalApis.apis().userList,
        headers: {
          Authorization: `JWT ${localStorage.getItem("JWT")}`,
        },
      })
        .then((response) => {
          console.log(response);
          this.userDatas = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    dialogDelete: function (item) {
      this.selectedUser = item;
      this.confirm = true;
    },
    close: function () {
      this.confirm = false;
    },
    deleteConfirm: function () {
      const id = this.selectedUser.id;
      console.log(id);
      axios({
        method: "delete",
        url: `${totalApis.apis().userDelete + id}/`,
        headers: {
          Authorization: `JWT ${localStorage.getItem("JWT")}`,
        },
      })
        .then((response) => {
          console.log(response);
          this.getUsers();
        })
        .catch((error) => {
          console.log(error);
        });
      this.confirm = false;
    },
    tokenCheck: function () {
      const token = localStorage.getItem("JWT");
      if (!token) {
        this.$router.push(totalPages.menuPages().SignIn);
      } else {
        this.tokenVerify();
      }
    },
    tokenVerify: function () {
      const token = localStorage.getItem("JWT");
      axios({
        method: "post",
        url: totalApis.apis().tokenVerify,
        data: {
          token: token,
        },
      })
        .then((response) => {
          console.log(response);
          this.tokenRefresh();
        })
        .catch((error) => {
          console.log(error);
          this.$router.push(totalPages.menuPages().SignIn);
        });
    },
    tokenRefresh: function () {
      const token = localStorage.getItem("JWT");
      axios({
        method: "post",
        url: totalApis.apis().tokenRefresh,
        data: {
          token: token,
        },
      })
        .then((response) => {
          console.log(response);
        })
        .catch((error) => {
          console.log(error);
          this.$router.push(totalPages.menuPages().SignIn);
        });
    },
  },
  mounted: function () {
    this.getUsers();
  },
  beforeMount: function () {
    this.tokenCheck();
  },
};
</script>
<style scoped>
#User {
  width: 100%;
  height: 100%;
}
#btnColor {
  border-color: #0474bd;
  background-color: #049cfc;
  color: white;
}
</style>
