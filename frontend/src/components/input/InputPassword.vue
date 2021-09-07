<template>
  <div id="InputPassword">
    <v-container>
      <div>
        <ValidationObserver ref="obs" v-slot="ObserverProps">
          <div>
            <div>
              <ValidationProvider
                :rules="totalPages.validateNames().requiredPassword"
                v-slot="{ errors }"
                :name="words.userPasswordEdit.password"
              >
                <v-text-field
                  :label="text1"
                  outlined
                  v-model="password"
                  :value="password"
                  :error-messages="errors"
                  :append-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'"
                  :type="showPassword ? 'text' : 'password'"
                  @click:append="showPassword = !showPassword"
                >
                </v-text-field>
              </ValidationProvider>
            </div>
          </div>

          <div>
            <div>
              <v-btn
                class="font-weight-bold primary lighten-1 float-left"
                @click="backPages"
              >
                {{ message1 }}
              </v-btn>
            </div>
            <div>
              <v-btn
                class="font-weight-bold primary lighten-1 float-right"
                :disabled="!ObserverProps.valid"
                @click="inputText"
              >
                {{ message2 }}
              </v-btn>
            </div>
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
  name: "InputPassword",
  data: () => ({
    totalPages: totalPages,
    words: words,
    password: "",
    showPassword: false,
  }),
  props: {
    text1: {
      type: String,
      default: "",
    },
    message1: {
      type: String,
      default: "",
    },
    message2: {
      type: String,
      default: "",
    },
  },
  methods: {
    inputText() {
      this.$emit("input-text", this.password);
      this.password = "";
    },
    backPages() {
      this.$emit("back-pages", 1);
    },
  },
};
</script>

<style>
#InputPassword {
  width: 100%;
  height: auto;
}
</style>
