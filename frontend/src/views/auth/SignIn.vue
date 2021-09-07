<template>
  <div id="SignIn" class="mt-5">
    <v-card
      :tile="$vuetify.breakpoint.sm || $vuetify.breakpoint.xs"
      class="mx-auto"
      flat
      max-width="640"
    >
      <v-card-title class="text-center pa-8">
        <h4>{{ words.signIn.title }}</h4>
      </v-card-title>
      <v-divider></v-divider>

      <div class="px-6 py-8">
        <div style="max-width: 344px" class="mx-auto">
          <div>
            <v-row>
              <v-col>
                <v-btn
                  class="text-capitalize caption primary lighten-1 white--text font-weight-bold"
                  height="48px"
                  width="100%"
                  outlined
                  style="border-color: #979797"
                  tile
                  @click="guestCreate"
                >
                  {{ words.signIn.guest }}
                </v-btn>
              </v-col>
            </v-row>

            <v-row>
              <v-col>
                <v-divider></v-divider>
              </v-col>
            </v-row>

            <ValidationObserver ref="obs" v-slot="ObserverProps">
              <v-row class="regist_info pt-6">
                <v-col>
                  <ValidationProvider
                    :rules="totalPages.validateNames().requiredEmail"
                    v-slot="{ errors }"
                    :name="words.signIn.mail"
                  >
                    <v-text-field
                      v-model="email"
                      dense
                      height="48px"
                      outlined
                      required
                      :error-messages="errors"
                      :label="words.signIn.mail"
                    ></v-text-field>
                  </ValidationProvider>

                  <ValidationProvider
                    :rules="totalPages.validateNames().requiredPassword"
                    v-slot="{ errors }"
                    :name="words.signIn.password"
                  >
                    <v-text-field
                      v-model="password"
                      dense
                      height="48px"
                      :append-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'"
                      :type="showPassword ? 'text' : 'password'"
                      outlined
                      required
                      :label="words.signIn.password"
                      :error-messages="errors"
                      @click:append="showPassword = !showPassword"
                    ></v-text-field>
                  </ValidationProvider>

                  <v-btn
                    class="caption"
                    color="#049cfc"
                    depressed
                    height="48px"
                    width="100%"
                    tile
                    :disabled="!ObserverProps.valid"
                    @click="login"
                  >
                    {{ words.signIn.login }}
                  </v-btn>
                </v-col>
              </v-row>
            </ValidationObserver>

            <v-row>
              <v-col>
                <v-divider></v-divider>
                <p @click="signUpSwitch">
                  <span class="blue--text">{{ words.signIn.signUp }}</span>
                  {{ words.signIn.message }}
                </p>
              </v-col>
            </v-row>
          </div>
        </div>
      </div>
    </v-card>
  </div>
</template>

<script>
import axios from "axios";
import totalPages from "@/common/totalPages.js";
import totalApis from "@/common/totalApis.js";
import words from "@/words/words.json";

export default {
  name: "SignIn",
  data: () => ({
    words: words,
    totalPages: totalPages,
    email: null,
    password: null,
    showPassword: false,
    guestName: null,
    guestEmail: null,
    guestPassword: null,
  }),
  methods: {
    signUpSwitch: function () {
      this.$router.push(totalPages.menuPages().SignUp);
    },
    login() {
      axios({
        method: "post",
        url: totalApis.apis().token,
        data: {
          email: this.email,
          password: this.password,
        },
      })
        .then((response) => {
          const status = response?.status;
          const result = response?.data;
          console.log(response);
          if (status == 200) {
            localStorage.setItem("JWT", result.token);
            console.log(localStorage.getItem("JWT"));
            this.getMyself();
          } else {
            console.log(response);
          }
        })
        .catch(function (error) {
          console.log(error);
        });
      this.email = "";
      this.password = "";
    },
    getMyself: function () {
      axios({
        method: "get",
        url: totalApis.apis().userMyself,
        headers: {
          Authorization: `JWT ${localStorage.getItem("JWT")}`,
        },
      })
        .then((response) => {
          const userData = response?.data;
          localStorage.setItem("userName", userData.name);
          console.log(localStorage.getItem("userName"));
          localStorage.setItem("userId", userData.id);
          console.log(localStorage.getItem("userId"));
          this.$router.push("/");
        })
        .catch(function (error) {
          this.tokenRefresh();
          console.log(error);
        });
    },
    guestCreate: function () {
      // ゲストユーザーのemail, name, passwordをランダムで生成
      this.guestEmail = Math.random().toString(32).substring(2) + "@example.com";
      const num = parseInt(Math.random() * 10000);
      this.guestName = "ゲストユーザー" + num;
      this.guestPassword =
        Math.random().toString(32).substring(2) + parseInt(Math.random() * 100);

      axios({
        method: "post",
        url: totalApis.apis().userCreate,
        data: {
          name: this.guestName,
          email: this.guestEmail,
          password: this.guestPassword,
        },
      })
        .then((response) => {
          console.log(response);
          this.guestLogin();
        })
        .catch((error) => {
          console.log(error);
        });
    },
    guestLogin: function () {
      axios({
        method: "post",
        url: totalApis.apis().token,
        data: {
          name: this.guestName,
          email: this.guestEmail,
          password: this.guestPassword,
        },
      })
        .then((response) => {
          console.log(response);
          const status = response?.status;
          const result = response?.data;
          if (status === 200) {
            localStorage.setItem("JWT", result.token);
            this.getMyself();
          } else {
            console.log(response);
          }
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>

<style scoped>
#SignIn {
  width: 100%;
  height: 100%;
}
</style>
