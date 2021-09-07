<template>
  <div id="task">
    <ValidationObserver ref="obs" v-slot="ObserverProps">
      <v-container>
        <v-form>
          <v-row>
            <v-col cols="6">
              <ValidationProvider
                :rules="totalPages.validateNames().required"
                v-slot="{ errors }"
                :name="words.task.taskName"
              >
                <v-text-field
                  v-model="taskName"
                  type="text"
                  autofocus
                  :label="words.task.taskName"
                  :error-messages="errors"
                >
                </v-text-field>
              </ValidationProvider>
            </v-col>
            <v-col cols="3">
              <ValidationProvider
                :rules="totalPages.validateNames().required"
                v-slot="{ errors }"
                :name="words.task.priority"
              >
                <v-select
                  :items="priority"
                  v-model="priorityValue"
                  @change="fetchPriority"
                  :error-messages="errors"
                  :label="words.task.priority"
                >
                </v-select>
              </ValidationProvider>
            </v-col>
            <v-col cols="3">
              <v-select
                :items="status"
                v-model="statusValue"
                @change="fetchStatus"
                :label="words.task.status"
              >
              </v-select>
            </v-col>
          </v-row>

          <v-row>
            <v-col cols="2">
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
                  <ValidationProvider
                    :rules="totalPages.validateNames().required"
                    :name="words.task.startDate"
                    v-slot="{ errors }"
                  >
                    <v-text-field
                      v-model="startDate"
                      :label="words.task.startDate"
                      prepend-icon="mdi-calendar"
                      readonly
                      :error-messages="errors"
                      v-bind="attrs"
                      v-on="on"
                    >
                    </v-text-field>
                  </ValidationProvider>
                </template>
                <v-date-picker v-model="startDate" scrollable header-color="primary">
                  <v-spacer></v-spacer>
                  <v-btn text color="primary" @click="menu = false">
                    {{ words.task.choices[0].cancel }}
                  </v-btn>
                  <v-btn text color="primary" @click="$refs.menu.save(startDate)">
                    {{ words.task.choices[1].ok }}
                  </v-btn>
                </v-date-picker>
              </v-menu>
            </v-col>

            <v-col cols="2">
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
                  <ValidationProvider
                    :rules="totalPages.validateNames().required"
                    :name="words.task.startTime"
                    v-slot="{ errors }"
                  >
                    <v-text-field
                      v-model="startTime"
                      :label="words.task.startTime"
                      prepend-icon="mdi-clock-time-four-outline"
                      readonly
                      :error-messages="errors"
                      v-bind="attrs"
                      v-on="on"
                    ></v-text-field>
                  </ValidationProvider>
                </template>
                <v-time-picker v-if="menu2" v-model="startTime" full-width>
                  <v-spacer></v-spacer>
                  <v-btn text color="primary" @click="menu2 = false">
                    {{ words.task.choices[0].cancel }}
                  </v-btn>
                  <v-btn text color="primary" @click="$refs.menu2.save(startTime)">
                    {{ words.task.choices[1].ok }}
                  </v-btn>
                </v-time-picker>
              </v-menu>
            </v-col>

            <v-col cols="2">
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
                  <ValidationProvider
                    :rules="totalPages.validateNames().required"
                    :name="words.task.endDate"
                    v-slot="{ errors }"
                  >
                    <v-text-field
                      v-model="endDate"
                      :label="words.task.endDate"
                      prepend-icon="mdi-calendar"
                      readonly
                      :error-messages="errors"
                      v-bind="attrs"
                      v-on="on"
                    >
                    </v-text-field>
                  </ValidationProvider>
                </template>
                <v-date-picker v-model="endDate" scrollable header-color="primary">
                  <v-spacer></v-spacer>
                  <v-btn text color="primary" @click="menu3 = false">
                    {{ words.task.choices[0].cancel }}
                  </v-btn>
                  <v-btn text color="primary" @click="$refs.menu3.save(endDate)">
                    {{ words.task.choices[1].ok }}
                  </v-btn>
                </v-date-picker>
              </v-menu>
            </v-col>

            <v-col cols="2">
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
                  <ValidationProvider
                    :rules="totalPages.validateNames().required"
                    :name="words.task.endTime"
                    v-slot="{ errors }"
                  >
                    <v-text-field
                      v-model="endTime"
                      :label="words.task.endTime"
                      prepend-icon="mdi-clock-time-four-outline"
                      readonly
                      :error-messages="errors"
                      v-bind="attrs"
                      v-on="on"
                    ></v-text-field>
                  </ValidationProvider>
                </template>
                <v-time-picker v-if="menu4" v-model="endTime" full-width>
                  <v-spacer></v-spacer>
                  <v-btn text color="primary" @click="menu4 = false">
                    {{ words.task.choices[0].cancel }}
                  </v-btn>
                  <v-btn text color="primary" @click="$refs.menu4.save(endTime)">
                    {{ words.task.choices[1].ok }}
                  </v-btn>
                </v-time-picker>
              </v-menu>
            </v-col>

            <v-col cols="4">
              <ValidationProvider
                :rules="totalPages.validateNames().required"
                v-slot="{ errors }"
                :name="words.task.name"
              >
                <v-select
                  :items="userInfo"
                  v-model="selected"
                  item-text="name"
                  item-value="id"
                  required
                  :error-messages="errors"
                  @change="fetchName"
                  :label="words.task.name"
                >
                </v-select>
              </ValidationProvider>
            </v-col>
          </v-row>

          <v-row>
            <v-col>
              <v-btn
                medium
                class="blue lighten-1 font-weight-bold white--text"
                :disabled="!ObserverProps.valid"
                @click="addTodo"
              >
                {{ words.task.add }}
              </v-btn>
            </v-col>
          </v-row>
        </v-form>
      </v-container>
    </ValidationObserver>

    <v-container>
      <v-card class="py-5">
        <v-row>
          <v-col>
            <v-card-title class="font-weight-bold">
              {{ words.task.list }}
              <v-spacer></v-spacer>
              <v-text-field
                v-model="search"
                append-icon="mdi-magnify"
                :label="words.task.search"
                single-line
                hide-details
              ></v-text-field>
            </v-card-title>
            <v-data-table
              :headers="headers"
              :items="tableDatas"
              :loading="loading"
              :search="search"
              locale="ja"
            >
              <template v-slot:[`item.priority`]="{ item }">
                <v-chip :color="getColor(item.priority)" dark>
                  {{ item.priority }}
                </v-chip>
              </template>
              <template v-slot:top>
                <v-dialog v-model="dialogEdit" fullscreen>
                  <v-card>
                    <v-card-title>
                      <span class="headline">{{ words.task.edit }}</span>
                    </v-card-title>
                    <v-card-text>
                      <v-container>
                        <v-row>
                          <v-col>
                            <v-text-field v-model="editedItem.task_name"> </v-text-field>
                          </v-col>
                        </v-row>

                        <v-row>
                          <v-col>
                            <v-select
                              :items="priority"
                              v-model="priorityValue"
                              @change="fetchPriority"
                              :label="editedItem.priority"
                            >
                            </v-select>
                          </v-col>

                          <v-col>
                            <v-select
                              :items="status"
                              v-model="statusValue"
                              @change="fetchStatus"
                              :label="editedItem.status"
                            ></v-select>
                          </v-col>
                        </v-row>

                        <v-row>
                          <v-col>
                            <v-menu
                              ref="menuEdit"
                              v-model="menuEdit"
                              :close-on-content-click="false"
                              :return-value.sync="startDateEdit"
                              transition="scale-transition"
                              persistent
                              offset-y
                              min-width="auto"
                            >
                              <template v-slot:activator="{ on, attrs }">
                                <v-text-field
                                  v-model="startDateEdit"
                                  :label="words.task.startDate"
                                  prepend-icon="mdi-calendar"
                                  readonly
                                  v-bind="attrs"
                                  v-on="on"
                                >
                                </v-text-field>
                              </template>
                              <v-date-picker
                                v-model="startDateEdit"
                                scrollable
                                header-color="primary"
                              >
                                <v-spacer></v-spacer>
                                <v-btn text color="primary" @click="menuEdit = false">
                                  {{ words.task.choices[0].cancel }}
                                </v-btn>
                                <v-btn
                                  text
                                  color="primary"
                                  @click="$refs.menuEdit.save(startDateEdit)"
                                >
                                  {{ words.task.choices[1].ok }}
                                </v-btn>
                              </v-date-picker>
                            </v-menu>
                          </v-col>

                          <v-col>
                            <v-menu
                              ref="menuEdit2"
                              v-model="menuEdit2"
                              :close-on-content-click="false"
                              :nudge-right="40"
                              :return-value.sync="startTimeEdit"
                              transition="scale-transition"
                              offset-y
                              max-width="290px"
                              min-width="290px"
                            >
                              <template v-slot:activator="{ on, attrs }">
                                <v-text-field
                                  v-model="startTimeEdit"
                                  :label="words.task.startTime"
                                  prepend-icon="mdi-clock-time-four-outline"
                                  readonly
                                  v-bind="attrs"
                                  v-on="on"
                                ></v-text-field>
                              </template>
                              <v-time-picker v-if="menuEdit2" v-model="startTimeEdit">
                                <v-spacer></v-spacer>
                                <v-btn text color="primary" @click="menuEdit2 = false">
                                  {{ words.task.choices[0].cancel }}
                                </v-btn>
                                <v-btn
                                  text
                                  color="primary"
                                  @click="$refs.menuEdit2.save(startTimeEdit)"
                                >
                                  {{ words.task.choices[1].ok }}
                                </v-btn>
                              </v-time-picker>
                            </v-menu>
                          </v-col>
                        </v-row>

                        <v-row>
                          <v-col>
                            <v-menu
                              ref="menuEdit3"
                              v-model="menuEdit3"
                              :close-on-content-click="false"
                              :return-value.sync="endDateEdit"
                              transition="scale-transition"
                              persistent
                              offset-y
                              min-width="auto"
                            >
                              <template v-slot:activator="{ on, attrs }">
                                <v-text-field
                                  v-model="endDateEdit"
                                  :label="words.task.endDate"
                                  prepend-icon="mdi-calendar"
                                  readonly
                                  v-bind="attrs"
                                  v-on="on"
                                >
                                </v-text-field>
                              </template>
                              <v-date-picker
                                v-model="endDateEdit"
                                scrollable
                                header-color="primary"
                              >
                                <v-spacer></v-spacer>
                                <v-btn text color="primary" @click="menuEdit3 = false">
                                  {{ words.task.choices[0].cancel }}
                                </v-btn>
                                <v-btn
                                  text
                                  color="primary"
                                  @click="$refs.menuEdit3.save(endDateEdit)"
                                >
                                  {{ words.task.choices[1].ok }}
                                </v-btn>
                              </v-date-picker>
                            </v-menu>
                          </v-col>

                          <v-col>
                            <v-menu
                              ref="menuEdit4"
                              v-model="menuEdit4"
                              :close-on-content-click="false"
                              :nudge-right="40"
                              :return-value.sync="endTimeEdit"
                              transition="scale-transition"
                              offset-y
                              max-width="290px"
                              min-width="290px"
                            >
                              <template v-slot:activator="{ on, attrs }">
                                <v-text-field
                                  v-model="endTimeEdit"
                                  :label="words.task.endTime"
                                  prepend-icon="mdi-clock-time-four-outline"
                                  readonly
                                  v-bind="attrs"
                                  v-on="on"
                                ></v-text-field>
                              </template>
                              <v-time-picker v-if="menuEdit4" v-model="endTimeEdit">
                                <v-spacer></v-spacer>
                                <v-btn text color="primary" @click="menuEdit4 = false">
                                  {{ words.task.choices[0].cancel }}
                                </v-btn>
                                <v-btn
                                  text
                                  color="primary"
                                  @click="$refs.menuEdit4.save(endTimeEdit)"
                                >
                                  {{ words.task.choices[1].ok }}
                                </v-btn>
                              </v-time-picker>
                            </v-menu>
                          </v-col>
                        </v-row>

                        <v-row>
                          <v-select
                            :items="userInfo"
                            v-model="selected"
                            item-text="name"
                            item-value="id"
                            @change="fetchName"
                            :label="editedItem.user_name"
                          >
                          </v-select>
                        </v-row>
                      </v-container>
                    </v-card-text>
                    <v-card-text>
                      <v-card-actions>
                        <v-btn @click="closeEdit">{{ words.task.close }}</v-btn>
                        <v-btn @click="updateEdit">{{ words.task.update }}</v-btn>
                        <v-spacer></v-spacer>
                      </v-card-actions>
                    </v-card-text>
                  </v-card>
                  <v-spacer></v-spacer>
                </v-dialog>
                <v-dialog v-model="dialogDelete" max-width="500px">
                  <v-card>
                    <v-card-title class="text-h5">{{
                      messages.task.confirm.delete
                    }}</v-card-title>
                    <v-card-actions>
                      <v-spacer></v-spacer>
                      <v-btn @click="closeDelete">{{ words.task.close }}</v-btn>
                      <v-btn
                        @click="deleteItemConfirm"
                        class="red lighten-1 white--text"
                        >{{ words.task.delete }}</v-btn
                      >
                      <v-spacer></v-spacer>
                    </v-card-actions>
                  </v-card>
                </v-dialog>
                <v-dialog v-model="dialogFinish" max-width="500px">
                  <v-card>
                    <v-card-title class="text-h5">{{
                      messages.task.confirm.finish
                    }}</v-card-title>
                    <v-card-actions>
                      <v-spacer></v-spacer>
                      <v-btn @click="closeFinish">{{ words.task.close }}</v-btn>
                      <v-btn
                        @click="finishItemConfirm"
                        class="blue lighten-1 white--text"
                        >{{ words.task.finish }}</v-btn
                      >
                      <v-spacer></v-spacer>
                    </v-card-actions>
                  </v-card>
                </v-dialog>
              </template>

              <template v-slot:[`item.actions`]="{ item }">
                <v-btn small @click="editItem(item)">
                  <v-icon>
                    {{ words.task.iconPencil }}
                  </v-icon>
                </v-btn>
                <v-btn small @click="deleteItem(item)">
                  <v-icon>
                    {{ words.task.iconDelete }}
                  </v-icon>
                </v-btn>
              </template>

              <template v-slot:[`item.finish`]="{ item }">
                <v-btn
                  small
                  class="blue lighten-1 font-weight-bold white--text"
                  @click="finishedItem(item)"
                >
                  {{ words.task.finish }}
                </v-btn>
              </template>
            </v-data-table>
          </v-col>
        </v-row>
      </v-card>
    </v-container>
  </div>
</template>

<script>
import axios from "axios";
import totalApis from "@/common/totalApis.js";
import totalPages from "@/common/totalPages.js";
import moment from "moment";
import messages from "@/messages/messages.json";
import words from "@/words/words.json";

export default {
  name: "task",
  data: () => ({
    words: words,
    messages: messages,
    totalPages: totalPages,
    dialogEdit: false,
    dialogDelete: false,
    dialogFinish: false,
    loading: false,
    search: "",
    taskName: "",
    priority: ["高い", "普通", "低い"],
    priorityValue: "",
    selectedPriority: null,
    status: ["未完了", "完了"],
    statusValue: "",
    selectedStatus: null,
    userInfo: [],
    selected: [],
    selectedName: null,
    startDate: null,
    endDate: null,
    startTime: null,
    endTime: null,
    taskData: null,
    menu: false,
    menu2: false,
    menu3: false,
    menu4: false,
    startDateEdit: null,
    startTimeEdit: null,
    endDateEdit: null,
    endTimeEdit: null,
    menuEdit: null,
    menuEdit2: null,
    menuEdit3: null,
    menuEdit4: null,
    headers: [
      { text: "ID", value: "task_id" },
      { text: "タスク名", value: "task_name" },
      { text: "緊急度", value: "priority" },
      { text: "状態", value: "status" },
      { text: "開始日", value: "start_date" },
      { text: "終了日", value: "end_date" },
      { text: "名前", value: "user_name" },
      { text: "編集 / 削除", value: "actions", sortable: false },
      { text: "完了", value: "finish", sortable: false },
    ],
    beforeDatas: [],
    tableDatas: [],
    editedItem: {
      task_name: "",
      priority: [],
      status: [],
      start_date: null,
      end_date: null,
      user_name: "",
    },
  }),
  methods: {
    fetchPriority(event) {
      this.selectedPriority = event;
    },
    fetchStatus(event) {
      this.selectedStatus = event;
    },
    fetchName(event) {
      this.selectedName = event;
    },
    getTasks: function () {
      axios({
        method: "get",
        url: totalApis.apis().taskList,
        headers: {
          Authorization: `JWT ${localStorage.getItem("JWT")}`,
        },
      })
        .then((response) => {
          this.beforeDatas = response?.data;
          this.tableDatas = this.beforeDatas;
          this.beforeDatas = this.beforeDatas.map((data) => {
            const result = this.userInfo.find(({ id }) => {
              return id === data.user_name;
            });
            data.user_name = result.name;
          });
        })
        .catch(function (error) {
          console.log(error);
        });
    },

    addTodo: function () {
      const startDateTime = moment(`${this.startDate} ${this.startTime}`);
      const endDateTime = moment(`${this.endDate} ${this.endTime}`);
      if (startDateTime > endDateTime) {
        return;
      }
      // 状態は未選択であれば、デフォルトで未完了に設定
      if (this.selectedStatus === null || "") {
        this.selectedStatus = "未完了";
      }

      axios({
        method: "post",
        url: totalApis.apis().taskCreate,
        headers: {
          Authorization: `JWT ${localStorage.getItem("JWT")}`,
        },
        data: {
          task_name: this.taskName,
          user_name: this.selectedName,
          status: this.selectedStatus,
          priority: this.selectedPriority,
          start_date: startDateTime,
          end_date: endDateTime,
        },
      })
        .then((response) => {
          console.log(response);
          this.taskName = null;
          this.selectedName = null;
          this.selectedPriority = "";
          this.priorityValue = "";
          this.selectedStatus = null;
          this.statusValue = "";
          this.startDate = null;
          this.startTime = null;
          this.endDate = null;
          this.endTime = null;
          this.selected = "";
          this.getTasks();
        })
        .catch(function (error) {
          console.log(error);
        });
    },

    editItem(item) {
      this.priorityValue = "";
      this.statusValue = "";
      this.editedItem = Object.assign({}, item);
      this.selectedPriority = this.editedItem.priority;
      this.selectedStatus = this.editedItem.status;
      this.startDateEdit = moment(this.editedItem.start_date).format("yyyy-MM-DD");
      this.startTimeEdit = moment(this.editedItem.start_date).format("HH:mm");
      this.endDateEdit = moment(this.editedItem.end_date).format("yyyy-MM-DD");
      this.endTimeEdit = moment(this.editedItem.end_date).format("HH:mm");
      this.dialogEdit = true;
    },

    deleteItem(item) {
      this.taskData = item;
      this.dialogDelete = true;
    },
    closeEdit: function () {
      this.selectedPriority = null;
      this.priorityValue = "";
      this.selectedStatus = null;
      this.statusValue = "";
      this.startDateEdit = null;
      this.endDateEdit = null;
      this.startTimeEdit = null;
      this.endTimeEdit = null;

      this.dialogEdit = false;
    },
    updateEdit: function () {
      const startDateTime = moment(`${this.startDateEdit} ${this.startTimeEdit}`);
      const endDateTime = moment(`${this.endDateEdit} ${this.endTimeEdit}`);
      const id = this.editedItem.task_id;
      const nameId = this.selectedName;
      const userName = this.editedItem.user_name;
      let user = null;

      // 名前を未選択の場合
      if (!nameId) {
        user = this.userInfo.find(({ name }) => {
          return name === userName;
        });
        user = user.id;
      } else {
        user = this.selectedName;
      }

      axios({
        method: "put",
        url: `${totalApis.apis().taskUpdate + id}/`,
        headers: {
          Authorization: `JWT ${localStorage.getItem("JWT")}`,
        },
        data: {
          task_name: this.editedItem.task_name,
          user_name: user,
          status: this.selectedStatus,
          priority: this.selectedPriority,
          start_date: startDateTime,
          end_date: endDateTime,
        },
      })
        .then((response) => {
          console.log(response);
          this.selectedName = null;
          this.priorityValue = "";
          this.statusValue = "";
          this.startDateEdit = null;
          this.startTimeEdit = null;
          this.endDateEdit = null;
          this.endTimeEdit = null;
          this.dialogEdit = false;
          this.getTasks();
        })
        .catch(function (error) {
          console.log(error);
        });
    },
    closeDelete: function () {
      this.dialogDelete = false;
    },
    deleteItemConfirm: function () {
      const id = this.taskData.task_id;
      axios({
        method: "delete",
        url: `${totalApis.apis().taskDelete + id}/`,
        headers: {
          Authorization: `JWT ${localStorage.getItem("JWT")}`,
        },
      })
        .then((response) => {
          console.log(response);
          this.getTasks();
        })
        .catch(function (error) {
          console.log(error);
        });
      this.dialogDelete = false;
    },
    getColor: function (item) {
      if (item === "高い") {
        return "red";
      } else if (item === "低い") {
        return "blue";
      } else {
        return "grey";
      }
    },
    getUserList: function () {
      const self = this;

      axios({
        method: "get",
        url: totalApis.apis().userList,
        headers: {
          Authorization: `JWT ${localStorage.getItem("JWT")}`,
        },
      })
        .then((response) => {
          const array = response?.data;

          for (const i in array) {
            const userId = array[i].id;
            const userNames = array[i].name;
            self.userInfo.push({ name: userNames, id: userId });
          }
          this.getTasks();
        })
        .catch(function (error) {
          console.log(error);
        });
    },
    finishedItem: function (item) {
      this.taskData = item;
      this.dialogFinish = true;
    },
    closeFinish: function () {
      this.dialogFinish = false;
    },
    finishItemConfirm: function () {
      const finish = "完了";
      const selectName = this.taskData.user_name;
      const selected = this.userInfo.find(({ name }) => {
        return name === selectName;
      });
      const id = this.taskData.task_id;
      axios({
        method: "put",
        url: `${totalApis.apis().taskUpdate + id}/`,
        headers: {
          Authorization: `JWT ${localStorage.getItem("JWT")}`,
        },
        data: {
          task_name: this.taskData.task_name,
          user_name: selected.id,
          status: finish,
          priority: this.taskData.priority,
          start_date: this.taskData.start_date,
          end_date: this.taskData.end_date,
        },
      })
        .then((response) => {
          console.log(response);
          this.getTasks();
        })
        .catch(function (error) {
          console.log(error);
        });
      this.dialogFinish = false;
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
  mounted: function () {
    this.getUserList();
  },
  beforeMount: function () {
    this.tokenCheck();
  },
};
</script>
<style scoped>
#task {
  width: 100%;
  height: 100%;
}
h1 {
  height: 50px;
}
</style>
