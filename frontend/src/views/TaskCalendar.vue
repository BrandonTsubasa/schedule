<template>
  <v-app>
    <div id="display">
      <v-container>
        <v-sheet tile height="6vh" color="grey lighten-3" class="d-flex align-center">
          <v-btn outlined small class="ma-4" @click="setToday">{{
            words.calendar.today
          }}</v-btn>
          <v-btn icon @click="$refs.calendar.prev()">
            <v-icon>{{ words.calendar.iconLeft }}</v-icon>
          </v-btn>
          <v-btn icon @click="$refs.calendar.next()">
            <v-icon>{{ words.calendar.iconRight }}</v-icon>
          </v-btn>
          <v-toolbar-title>{{ title }}</v-toolbar-title>

          <v-select
            v-model="type"
            :items="types"
            dense
            outlined
            hide-details
            class="ma-2"
            label="type"
          ></v-select>
        </v-sheet>
        <v-sheet height="90vh" width="auto">
          <v-calendar
            ref="calendar"
            v-model="value"
            color="orange lighten-3"
            :type="type"
            :events="events"
            :event-color="getEventColor"
            locale="ja-jp"
            :day-format="(timestamp) => new Date(timestamp.date).getDate()"
            :month-format="(timestamp) => new Date(timestamp.date).getMonth() + 1 + ' /'"
            @change="getTaskCal"
            @click:event="showEvent"
          >
          </v-calendar>
          <v-dialog v-model="editDialog" fullscreen>
            <v-card>
              <v-card-title class="text-h5">{{ words.calendar.edit }}</v-card-title>
              <v-card-text>
                <v-container>
                  <v-row>
                    <v-col>
                      <v-text-field
                        v-model="editedItem.task_name"
                        :label="words.calendar.task"
                      ></v-text-field>
                    </v-col>
                  </v-row>

                  <v-row>
                    <v-col>
                      <v-select
                        :items="priority"
                        @change="fetchPriority"
                        v-model="priorityValue"
                        :label="editedItem.priority"
                      >
                      </v-select>
                    </v-col>

                    <v-col>
                      <v-select
                        :items="status"
                        @change="fetchStatus"
                        v-model="statusValue"
                        :label="editedItem.status"
                      >
                      </v-select>
                    </v-col>
                  </v-row>

                  <v-row>
                    <v-col>
                      <v-menu
                        ref="menu"
                        v-model="menu"
                        :close-on-content-click="false"
                        :return-value.sync="startDate"
                        transition="scale-transition"
                        persistent
                        offset-y
                        min-width="auto"
                      >
                        <template v-slot:activator="{ on, attrs }">
                          <v-text-field
                            v-model="startDate"
                            :label="words.calendar.startDate"
                            prepend-icon="mdi-calendar"
                            readonly
                            v-bind="attrs"
                            v-on="on"
                          >
                          </v-text-field>
                        </template>
                        <v-date-picker
                          v-model="startDate"
                          scrollable
                          header-color="primary"
                        >
                          <v-spacer></v-spacer>
                          <v-btn text color="primary" @click="menu = false">
                            {{ words.calendar.choices[0].cancel }}
                          </v-btn>
                          <v-btn text color="primary" @click="$refs.menu.save(startDate)">
                            {{ words.calendar.choices[1].ok }}
                          </v-btn>
                        </v-date-picker>
                      </v-menu>
                    </v-col>

                    <v-col>
                      <v-menu
                        ref="menu2"
                        v-model="menu2"
                        :close-on-content-click="false"
                        :nudge-right="40"
                        :return-value.sync="startTime"
                        transition="scale-transition"
                        offset-y
                        max-width="290px"
                        min-width="290px"
                      >
                        <template v-slot:activator="{ on, attrs }">
                          <v-text-field
                            v-model="startTime"
                            :label="words.calendar.startTime"
                            prepend-icon="mdi-clock-time-four-outline"
                            readonly
                            v-bind="attrs"
                            v-on="on"
                          ></v-text-field>
                        </template>
                        <v-time-picker v-if="menu2" v-model="startTime" full-width>
                          <v-spacer></v-spacer>
                          <v-btn text color="primary" @click="menu2 = false">
                            {{ words.calendar.choices[0].cancel }}
                          </v-btn>
                          <v-btn
                            text
                            color="primary"
                            @click="$refs.menu2.save(startTime)"
                          >
                            {{ words.calendar.choices[1].ok }}
                          </v-btn>
                        </v-time-picker>
                      </v-menu>
                    </v-col>
                  </v-row>

                  <v-row>
                    <v-col>
                      <v-menu
                        ref="menu3"
                        v-model="menu3"
                        :close-on-content-click="false"
                        :return-value.sync="endDate"
                        transition="scale-transition"
                        persistent
                        offset-y
                        min-width="auto"
                      >
                        <template v-slot:activator="{ on, attrs }">
                          <v-text-field
                            v-model="endDate"
                            :label="words.calendar.endDate"
                            prepend-icon="mdi-calendar"
                            readonly
                            v-bind="attrs"
                            v-on="on"
                          >
                          </v-text-field>
                        </template>
                        <v-date-picker
                          v-model="endDate"
                          scrollable
                          header-color="primary"
                        >
                          <v-spacer></v-spacer>
                          <v-btn text color="primary" @click="menu3 = false">
                            {{ words.calendar.choices[0].cancel }}
                          </v-btn>
                          <v-btn text color="primary" @click="$refs.menu3.save(endDate)">
                            {{ words.calendar.choices[1].ok }}
                          </v-btn>
                        </v-date-picker>
                      </v-menu>
                    </v-col>

                    <v-col>
                      <v-menu
                        ref="menu4"
                        v-model="menu4"
                        :close-on-content-click="false"
                        :nudge-right="40"
                        :return-value.sync="endTime"
                        transition="scale-transition"
                        offset-y
                        max-width="290px"
                        min-width="290px"
                      >
                        <template v-slot:activator="{ on, attrs }">
                          <v-text-field
                            v-model="endTime"
                            :label="words.calendar.endTime"
                            prepend-icon="mdi-clock-time-four-outline"
                            readonly
                            v-bind="attrs"
                            v-on="on"
                          ></v-text-field>
                        </template>
                        <v-time-picker v-if="menu4" v-model="endTime" full-width>
                          <v-spacer></v-spacer>
                          <v-btn text color="primary" @click="menu4 = false">
                            {{ words.calendar.choices[0].cancel }}
                          </v-btn>
                          <v-btn text color="primary" @click="$refs.menu4.save(endTime)">
                            {{ words.calendar.choices[1].ok }}
                          </v-btn>
                        </v-time-picker>
                      </v-menu>
                    </v-col>
                  </v-row>
                </v-container>
              </v-card-text>

              <v-card-actions>
                <v-btn @click="close">{{ words.calendar.close }}</v-btn>
                <v-spacer></v-spacer>
                <v-btn @click="updateEdit">{{ words.calendar.update }}</v-btn>
                <v-btn @click="deleteEdit" class="red white--text">{{
                  words.calendar.delete
                }}</v-btn>
              </v-card-actions>
            </v-card>
          </v-dialog>
        </v-sheet>
      </v-container>
    </div>
  </v-app>
</template>

<script>
import axios from "axios";
import moment from "moment";
import totalApis from "@/common/totalApis.js";
import totalPages from "@/common/totalPages.js";
import words from "@/words/words.json";

export default {
  data: () => ({
    words: words,
    allTasks: [],
    editDialog: false,
    editedItem: {
      task_id: null,
      task_name: null,
      priority: [],
      priorityValue: "",
      status: [],
      statusValue: "",
      start_date: null,
      end_date: null,
      user_name: null,
    },
    taskName: "",
    priority: ["高い", "普通", "低い"],
    selectedPriority: null,
    status: ["未完了", "完了"],
    selectedStatus: null,
    startDate: null,
    menu: false,
    startTime: null,
    menu2: null,
    endDate: null,
    menu3: null,
    endTime: null,
    menu4: null,
    events: [],
    value: moment().format("yyyy-MM-DD"),
    type: "month",
    types: ["month", "week", "day"],
  }),
  computed: {
    title() {
      return moment(this.value).format("yyyy年 M月");
    },
  },
  methods: {
    getTaskCal: function () {
      axios({
        method: "get",
        url: totalApis.apis().taskList,
        headers: {
          Authorization: `JWT ${localStorage.getItem("JWT")}`,
        },
      })
        .then((response) => {
          const result = response?.data;
          this.events = null;
          this.allTasks = result;
          const events = [];
          const mySelf = Number(localStorage.getItem("userId"));

          result.forEach(function (element, index) {
            // ユーザー自身のタスク
            if (mySelf === result[index].user_name) {
              if (result[index].priority === "高い") {
                events[index] = {
                  name: element.task_name,
                  start: element.start_date,
                  end: element.end_date,
                  color: "red",
                };
              } else if (result[index].priority === "低い") {
                events[index] = {
                  name: element.task_name,
                  start: element.start_date,
                  end: element.end_date,
                  color: "blue",
                };
              } else {
                events[index] = {
                  name: element.task_name,
                  start: element.start_date,
                  end: element.end_date,
                  color: "grey",
                };
              }
            }
          });
          this.events = events;
        })
        .catch(function (error) {
          console.log(error);
        });
    },
    setToday() {
      this.value = moment().format("yyyy-MM-DD");
    },
    showEvent: function (item) {
      const selectedData = item;
      const Tasks = this.allTasks;
      let events = null;
      // 選択したタスクを検索
      Tasks.forEach(function (element, index) {
        if (selectedData.event.name === Tasks[index].task_name) {
          events = {
            task_id: element.task_id,
            task_name: element.task_name,
            priority: element.priority,
            status: element.status,
            start_date: element.start_date,
            end_date: element.end_date,
            user_name: element.user_name,
          };
        }
      });
      // 選択したタスクを初期値に代入
      this.editedItem = Object.assign({}, events);
      this.selectedPriority = this.editedItem.priority;
      this.priorityValue = "";
      this.selectedStatus = this.editedItem.status;
      this.statusValue = "";
      this.startDate = moment(this.editedItem.start_date).format("yyyy-MM-DD");
      this.startTime = moment(this.editedItem.start_date).format("HH:mm");
      this.endDate = moment(this.editedItem.end_date).format("yyyy-MM-DD");
      this.endTime = moment(this.editedItem.end_date).format("HH:mm");

      this.editDialog = true;
    },
    getEventColor(event) {
      return event.color;
    },
    fetchPriority: function (event) {
      this.selectedPriority = event;
    },
    fetchStatus: function (event) {
      this.selectedStatus = event;
    },
    close: function () {
      this.editDialog = false;
    },
    updateEdit: function () {
      const id = this.editedItem.task_id;
      const startDateTime = moment(`${this.startDate} ${this.startTime}`);
      console.log(startDateTime);
      const endDateTime = moment(`${this.endDate} ${this.endTime}`);
      console.log(endDateTime);

      axios({
        method: "put",
        url: `${totalApis.apis().taskUpdate + id}/`,
        headers: {
          Authorization: `JWT ${localStorage.getItem("JWT")}`,
        },
        data: {
          task_name: this.editedItem.task_name,
          user_name: this.editedItem.user_name,
          status: this.selectedStatus,
          priority: this.selectedPriority,
          start_date: startDateTime,
          end_date: endDateTime,
        },
      })
        .then((response) => {
          console.log(response);
          this.getTaskCal();
        })
        .catch((error) => {
          console.log(error);
        });

      this.editDialog = false;
    },
    deleteEdit: function () {
      const id = this.editedItem.task_id;
      axios({
        method: "delete",
        url: `${totalApis.apis().taskDelete + id}/`,
        headers: {
          Authorization: `JWT ${localStorage.getItem("JWT")}`,
        },
      })
        .then((response) => {
          console.log(response);
          this.getTaskCal();
        })
        .catch((error) => {
          console.log(error);
        });

      this.editDialog = false;
    },

    tokenCheck: function () {
      const token = localStorage.getItem("JWT");
      if (!token) {
        this.$router.push(totalPages.menuPages().SignIn);
      } else {
        this.tokenVerify();
      }
    },
    tokenVerify: function () {
      const token = localStorage.getItem("JWT");
      axios({
        method: "post",
        url: totalApis.apis().tokenVerify,
        data: {
          token: token,
        },
      })
        .then((response) => {
          console.log(response);
          this.tokenRefresh();
        })
        .catch((error) => {
          console.log(error);
          this.$router.push(totalPages.menuPages().SignIn);
        });
    },
    tokenRefresh: function () {
      const token = localStorage.getItem("JWT");
      axios({
        method: "post",
        url: totalApis.apis().tokenRefresh,
        data: {
          token: token,
        },
      })
        .then((response) => {
          console.log(response);
        })
        .catch((error) => {
          console.log(error);
          this.$router.push(totalPages.menuPages().SignIn);
        });
    },
  },
  beforeMount: function () {
    this.tokenCheck();
  },
};
</script>

<style>
#display {
  width: 100%;
  height: 100%;
}
</style>
