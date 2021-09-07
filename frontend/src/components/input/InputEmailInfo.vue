<template>
  <div id="InputEmailInfo">
    <v-container>
      <div>
        <ValidationObserver ref="obs" v-slot="ObserverProps">
          <div>
            <ValidationProvider
              :rules="totalPages.validateNames().required"
              v-slot="{ errors }"
              :name="words.userEmailEdit.name"
            >
              <v-text-field
                :label="text1"
                outlined
                v-model="inputUser"
                :value="inputUser"
                :error-messages="errors"
              >
              </v-text-field>
            </ValidationProvider>
          </div>

          <div>
            <ValidationProvider
              :rules="totalPages.validateNames().requiredPassword"
              v-slot="{ errors }"
              :name="words.userEmailEdit.password"
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
  name: "InputEmailInfo",
  data: () => ({
    totalPages: totalPages,
    words: words,
    inputUser: null,
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
      this.$emit("input-text", this.inputUser, this.inputPassword);
      this.inputUser = "";
      this.inputPassword = "";
    },
  },
};
</script>

<style>
#InputEmailInfo {
  width: 100%;
  height: auto;
}
</style>
