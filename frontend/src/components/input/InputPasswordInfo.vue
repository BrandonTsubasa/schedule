<template>
  <div id="InputPasswordInfo">
    <v-container>
      <div>
        <ValidationObserver ref="obs" v-slot="ObserverProps">
          <div>
            <ValidationProvider
              :rules="totalPages.validateNames().required"
              v-slot="{ errors }"
              :name="words.userPasswordEdit.name"
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
              :rules="totalPages.validateNames().requiredEmail"
              v-slot="{ errors }"
              :name="words.userPasswordEdit.mail"
            >
              <v-text-field
                :label="text2"
                outlined
                v-model="inputMail"
                :value="inputMail"
                :error-messages="errors"
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
  name: "InputPasswordInfo",
  data: () => ({
    totalPages: totalPages,
    words: words,
    inputUser: null,
    inputMail: null,
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
      this.$emit("input-text", this.inputUser, this.inputMail);
      this.inputUser = "";
      this.inputMail = "";
    },
  },
};
</script>

<style>
#InputPasswordInfo {
  width: 100%;
  height: auto;
}
</style>
