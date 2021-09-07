<template>
  <div id="UserName">
    <v-container class="mt-10" v-if="pages === 1">
      <v-card>
        <v-row justify="center" class="pt-5">
          <v-col cols="8">
            <InputNameInfo
              :text1="words.userNameEdit.mail"
              :inputEmail="email"
              :text2="words.userNameEdit.password"
              :inputPassword="password"
              :message="words.userNameEdit.next"
              @input-text="addTwoInfos"
            />
          </v-col>
        </v-row>
      </v-card>
    </v-container>

    <v-container class="mt-10" v-if="pages === 2">
      <v-card>
        <v-row justify="center" class="pt-5">
          <v-col cols="8">
            <InputName
              :text1="words.userNameEdit.name"
              :inputUser="user"
              :message1="words.userNameEdit.back"
              @back-pages="back"
              :message2="words.userNameEdit.next"
              @input-text="addInfo"
            />
          </v-col>
        </v-row>
      </v-card>
    </v-container>

    <v-container class="mt-10" v-if="pages === 3">
      <v-card>
        <v-row justify="center" class="pt-5">
          <v-col cols="8">
            <Confirm
              :userName="user"
              :mail="email"
              :password="password"
              @back="returnPages"
              @update-name="update"
            />
          </v-col>
        </v-row>
      </v-card>
    </v-container>
  </div>
</template>

<script>
import axios from "axios";
import Confirm from "@/components/confirm/Confirm.vue";
import InputNameInfo from "@/components/input/InputNameInfo.vue";
import InputName from "@/components/input/InputName.vue";
import totalApis from "@/common/totalApis.js";
import totalPages from "@/common/totalPages.js";
import words from "@/words/words.json";

export default {
  name: "UserNameEdit",
  data: () => ({
    words: words,
    totalPages: totalPages,
    pages: 1,
    user: "",
    email: "",
    password: "",
    getMail: "",
  }),
  components: {
    InputNameInfo,
    InputName,
    Confirm,
  },
  methods: {
    addTwoInfos: function (value1, value2) {
      this.email = value1;
      this.password = value2;
      console.log(this.email);
      console.log(this.password);
      this.pages++;
    },
    addInfo: function (value) {
      this.user = value;
      this.pages++;
    },
    back: function (value) {
      this.user = "";
      const i = value;
      this.pages = this.pages - i;
    },
    returnPages: function (value) {
      const i = value;
      this.pages = this.pages - i;
    },
    update: function (value1, value2, value3) {
      const newName = value1;
      const newEmail = value2;
      const newPassword = value3;

      axios({
        method: "put",
        url: totalApis.apis().userMyself,
        headers: {
          Authorization: `JWT ${localStorage.getItem("JWT")}`,
        },
        data: {
          email: newEmail,
          name: newName,
          password: newPassword,
        },
      })
        .then((response) => {
          console.log(response);
        })
        .catch((error) => {
          console.log(error);
        });
      this.user = "";
      this.mail = "";
      this.password = "";

      this.$router.push(totalPages.pages().Top);
    },
  },
  beforeMount: function () {
    axios({
      method: "get",
      url: totalApis.apis().userMyself,
      headers: {
        Authorization: `JWT ${localStorage.getItem("JWT")}`,
      },
    })
      .then((response) => {
        this.getMail = response?.data?.email;
      })
      .catch((error) => {
        console.log(error);
      });
  },
};
</script>

<style scoped>
#UserName {
  width: 100%;
  height: 100%;
}
</style>
