<template>
  <div id="InputEmail">
    <v-container>
      <div>
        <ValidationObserver ref="obs" v-slot="ObserverProps">
          <div>
            <ValidationProvider
              :rules="totalPages.validateNames().requiredEmail"
              v-slot="{ errors }"
              :name="words.userEmailEdit.mail"
            >
              <v-text-field
                :label="text1"
                outlined
                v-model="mail"
                :value="mail"
                :error-messages="errors"
              >
              </v-text-field>
            </ValidationProvider>
          </div>

          <div>
            <v-row>
              <v-col>
                <v-btn
                  class="font-weight-bold primary lighten-1 float-left"
                  @click="backPages"
                >
                  {{ message1 }}
                </v-btn>
              </v-col>
              <v-col>
                <v-btn
                  class="font-weight-bold primary lighten-1 float-right"
                  :disabled="!ObserverProps.valid"
                  @click="inputText"
                >
                  {{ message2 }}
                </v-btn>
              </v-col>
            </v-row>
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
  name: "InputEmail",
  data: () => ({
    totalPages: totalPages,
    words: words,
    mail: "",
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
      this.$emit("input-text", this.mail);
      this.mail = "";
    },
    backPages() {
      this.$emit("back-pages", 1);
    },
  },
};
</script>

<style>
#InputEmail {
  width: 100%;
  height: auto;
}
</style>
