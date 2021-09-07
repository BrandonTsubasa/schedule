<template>
  <div id="SignUp" class="mt-5">
    <v-card
      :tile="$vuetify.breakpoint.sm || $vuetify.breakpoint.xs"
      class="mx-auto"
      flat
      max-width="640"
    >
      <v-card-title class="text-center pa-8">
        <h4>{{ words.signup.title }}</h4>
      </v-card-title>
      <v-divider> </v-divider>

      <div class="px-6 py-8">
        <div style="max-width: 344px" class="mx-auto">
          <div>
            <ValidationObserver ref="obs" v-slot="ObserverProps">
              <v-row class="regist_info pt-6">
                <v-col>
                  <ValidationProvider
                    :rules="totalPages.validateNames().required"
                    v-slot="{ errors }"
                    :name="words.signup.userName"
                  >
                    <v-text-field
                      v-model="userName"
                      autofocus
                      dense
                      height="48px"
                      outlined
                      required
                      :error-messages="errors"
                      :label="words.signup.userName"
                    ></v-text-field>
                  </ValidationProvider>

                  <ValidationProvider
                    :rules="totalPages.validateNames().requiredEmail"
                    v-slot="{ errors }"
                    :name="words.signup.mail"
                  >
                    <v-text-field
                      v-model="email"
                      dense
                      height="48px"
                      outlined
                      required
                      :error-messages="errors"
                      :label="words.signup.mail"
                    ></v-text-field>
                  </ValidationProvider>

                  <ValidationProvider
                    :rules="`${
                      totalPages.validateNames().requiredConfirm
                    }password|min:6|max:20`"
                    v-slot="{ errors }"
                    :name="words.signup.password"
                  >
                    <v-text-field
                      v-model="password"
                      dense
                      height="48px"
                      :append-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'"
                      :type="showPassword ? 'text' : 'password'"
                      outlined
                      required
                      :error-messages="errors"
                      :label="words.signup.password"
                      @click:append="showPassword = !showPassword"
                      counter="20"
                    ></v-text-field>
                  </ValidationProvider>

                  <ValidationProvider v-slot="{ errors }" vid="password">
                    <v-text-field
                      v-model="passwordConfirm"
                      dense
                      height="48px"
                      :append-icon="showPasswordConfirm ? 'mdi-eye' : 'mdi-eye-off'"
                      :type="showPasswordConfirm ? 'text' : 'password'"
                      outlined
                      required
                      :error-messages="errors"
                      :label="words.signup.passwordConfirm"
                      @click:append="showPasswordConfirm = !showPasswordConfirm"
                      counter="20"
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
                    @click="regist"
                  >
                    {{ words.signup.regist }}
                  </v-btn>
                </v-col>
              </v-row>
            </ValidationObserver>

            <v-row>
              <v-col>
                <v-divider></v-divider>
                <p @click="signInSwitch">
                  <span class="blue--text">{{ words.signup.login }}</span>
                  {{ words.signup.message }}
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
  name: "SignUp",
  data: () => ({
    words: words,
    totalPages: totalPages,
    userName: null,
    email: null,
    password: null,
    passwordConfirm: null,
    showPassword: false,
    showPasswordConfirm: false,
  }),
  methods: {
    signInSwitch: function () {
      this.$router.push(totalPages.menuPages().SignIn);
    },
    regist() {
      if (this.password !== this.passwordConfirm) {
        return;
      }

      axios({
        method: "post",
        url: totalApis.apis().userCreate,
        data: {
          name: this.userName,
          email: this.email,
          password: this.password,
        },
      })
        .then((response) => {
          console.log(response);
          this.userName = "";
          this.email = "";
          this.password = "";
          this.passwordConfirm = "";
          this.$router.push(totalPages.menuPages().SignIn);
        })
        .catch(function (error) {
          console.log(error);
        });
    },
  },
};
</script>

<style scoped>
#SignUp {
  width: 100%;
  height: 100%;
}
</style>
