<template>
  <div id="InputUserName">
    <v-container>
      <div>
        <ValidationObserver ref="obs" v-slot="ObserverProps">
          <ValidationProvider
            :rules="totalPages.validateNames().required"
            v-slot="{ errors }"
            :name="words.userNameEdit.name"
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
        </ValidationObserver>
      </div>
    </v-container>
  </div>
</template>

<script>
import totalPages from "@/common/totalPages.js";
import words from "@/words/words.json";

export default {
  name: "InputUserName",
  data: () => ({
    totalPages: totalPages,
    words: words,
    inputUser: "",
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
      this.$emit("input-text", this.inputUser);
      this.inputUser = "";
    },
    backPages() {
      this.$emit("back-pages", 1);
    },
  },
};
</script>

<style>
#InputUserName {
  width: 100%;
  height: auto;
}
</style>
