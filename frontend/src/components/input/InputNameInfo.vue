<template>
  <div id="InputNameInfo">
    <v-container>
      <div>
        <ValidationObserver ref="obs" v-slot="ObserverProps">
          <div>
            <ValidationProvider
              :rules="totalPages.validateNames().requiredEmail"
              v-slot="{ errors }"
              :name="words.userNameEdit.mail"
            >
              <v-text-field
                :label="text1"
                outlined
                v-model="inputEmail"
                :value="inputEmail"
                :error-messages="errors"
              >
              </v-text-field>
            </ValidationProvider>
          </div>

          <div>
            <ValidationProvider
              :rules="totalPages.validateNames().requiredPassword"
              v-slot="{ errors }"
              :name="words.userNameEdit.password"
            >
              <v-text-field
                :label="text2"
                outlined
                v-model="inputPassword"
                :value="inputPassword"
                :append-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'"
                :type="showPassword ? 'text' : 'password'"
                :error-messages="errors"
                @click:append="showPassword = !showPassword"
              >
              </v-text-field>
            </ValidationProvider>
          </div>

          <div>
            <v-btn
              class="font-weight-bold primary lighten-1 float-right"
              :disabled="!ObserverProps.valid"
              @click="inputText"
            >
              {{ message }}
            </v-btn>
          </div>
        </ValidationObserver>
      </div>
    </v-container>
  </div>
</template>

<script>
import totalPages from "@/common/totalPages.js";
import words from "@/words/words.json";

export default {
  name: "InputNameInfo",
  data: () => ({
    totalPages: totalPages,
    words: words,
    inputEmail: null,
    inputPassword: null,
    showPassword: false,
  }),
  props: {
    text1: {
      type: String,
      default: "",
    },
    text2: {
      type: String,
      default: "",
    },
    message: {
      type: String,
      default: "",
    },
  },
  methods: {
    inputText() {
      this.$emit("input-text", this.inputEmail, this.inputPassword);
      this.inputEmail = "";
      this.inputPassword = "";
    },
  },
};
</script>

<style>
#InputNameInfo {
  width: 100%;
  height: auto;
}
</style>
