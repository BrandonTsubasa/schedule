<template>
  <div id="UserName">
    <v-container class="mt-10" v-if="pages === 1">
      <v-card>
        <v-row justify="center" class="pt-5">
          <v-col cols="8">
            <InputPasswordInfo
              :text1="words.userPasswordEdit.name"
              :text2="words.userPasswordEdit.mail"
              :message="words.userPasswordEdit.next"
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
            <InputPassword
              :text1="words.userPasswordEdit.password"
              :message1="words.userPasswordEdit.back"
              :password="password"
              @back-pages="back"
              :message2="words.userPasswordEdit.next"
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
import InputPasswordInfo from "@/components/input/InputPasswordInfo.vue";
import InputPassword from "@/components/input/InputPassword.vue";
import Confirm from "@/components/confirm/Confirm.vue";
import totalApis from "@/common/totalApis.js";
import totalPages from "@/common/totalPages.js";
import words from "@/words/words.json";

export default {
  name: "UserPasswordEdit",
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
    InputPasswordInfo,
    InputPassword,
    Confirm,
  },
  methods: {
    addTwoInfos: function (value1, value2) {
      this.user = value1;
      this.email = value2;
      console.log(this.user);
      console.log(this.email);
      this.pages++;
    },
    addInfo: function (value) {
      this.password = value;
      console.log(this.password);
      this.pages++;
    },
    back: function (value) {
      this.password = "";
      const i = value;
      this.pages = this.pages - i;
    },
    returnPages: function (value) {
      const i = value;
      this.pages = this.pages - i;
    },
    update: function (value1, value2, value3) {
      const newName = value1;
      console.log(newName);
      const newEmail = value2;
      console.log(newEmail);
      const newPassword = value3;
      console.log(newPassword);

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
