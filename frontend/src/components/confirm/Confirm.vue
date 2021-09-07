<template>
  <div id="Confirm">
    <v-container>
      <div>
        {{ item }}
        <v-simple-table>
          <template v-slot:default>
            <thead>
              <tr>
                <th class="text-left">
                  {{ words.confirm.name }}
                </th>
                <th class="text-left">
                  {{ words.confirm.mail }}
                </th>
                <th class="text-left">
                  {{ words.confirm.password }}
                </th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>{{ userName }}</td>
                <td>{{ mail }}</td>
                <td>{{ password }}</td>
              </tr>
            </tbody>
          </template>
        </v-simple-table>
        <div class="float-left mt-5">
          <v-btn class="primary lighten-1 font-weight-bold" @click="back">
            {{ words.confirm.back }}
          </v-btn>
        </div>

        <div class="float-right mt-5">
          <v-btn class="primary lighten-1 font-weight-bold" @click="updateName">
            {{ words.confirm.update }}
          </v-btn>
        </div>
      </div>
    </v-container>
  </div>
</template>

<script>
import totalPages from "@/common/totalPages.js";
import words from "@/words/words.json";

export default {
  name: "Confirm",
  data: () => ({
    totalPages: totalPages,
    words: words,
    userName: "",
    mail: "",
    password: "",
  }),
  props: {
    userName: {
      type: String,
      default: "",
    },
    mail: {
      type: String,
      default: "",
    },
    password: {
      type: String,
      default: "",
    },
  },
  methods: {
    back: function () {
      this.$emit("back", 1);
    },
    updateName: function () {
      this.$emit("update-name", this.userName, this.mail, this.password);
    },
  },
};
</script>

<style>
#Confirm {
  width: 100%;
  height: auto;
}
</style>
