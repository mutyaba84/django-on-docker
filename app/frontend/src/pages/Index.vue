<template>
  <q-page class="row items-center justify-evenly">
    <div class="home">
      <hr />

      <div class="columns">
        <div class="column is-3 is-offset-3">
          <form v-on:submit.prevent="addVariable">
            <h2 class="subtitle">Variable</h2>

            <div class="container-fluid">
              <label class="label">name</label>
              <div class="control">
                <input class="input" type="text" v-model="name" />
              </div>
            </div>

            <div class="field">
              <label class="label">Type</label>
              <div class="control">
                <div class="select">
                  <select v-model="type">
                    <option value="string">string</option>
                    <option value="boolean">boolean</option>
                  </select>
                </div>
              </div>
            </div>

            <div class="field">
              <div class="control">
                <button class="button is-link">Submit</button>
              </div>
            </div>
          </form>
        </div>
      </div>

      <div class="columns">
        <div class="column is-6">
          <h2 class="subtitle">String</h2>

          <div class="string">
            <div
              class="card"
              v-for="variable in variables"
              v-if="variable.status === 'String'"
              v-bind:key="variable.id"
            >
              <div class="card-content">{{ variable.name }}</div>

              <footer class="card-footer">
                <a
                  class="card-footer-item"
                  @click="setStatus(variable.id, 'boolean')"
                  >boolean</a
                >
              </footer>
            </div>
          </div>
        </div>
        <div class="column is-6">
          <h2 class="subtitle">boolean</h2>

          <div class="boolean">
            <div
              class="card"
              v-for="variable in variables"
              v-if="variable.type === 'boolean'"
              v-bind:key="variable.id"
            >
              <div class="card-content">{{ variable.name }}</div>

              <footer class="card-footer">
                <a
                  class="card-footer-item"
                  @click="setType(variable.id, 'string')"
                  >String</a
                >
              </footer>
            </div>
          </div>
        </div>
      </div>
    </div>
  </q-page>
</template>

<script>
const API_URL = 'http://127.0.0.1:8000/';
import axios from 'axios';

export default {
  name: 'Home',
  data() {
    return {
      Variable: [],
      name: 'name',
      type: 'string'
    };
  },
  mounted() {
    this.getVariable();
  },
  methods: {
    getVariable() {
      axios({
        method: 'get',
        url: API_URL + 'Variable/',
        auth: {
          username: 'admin',
          password: 'After7'
        }
      }).then(response => (this.Variables = response.data));
    },
    addVariable() {
      if (this.name) {
        axios({
          method: 'post',
          url: API_URL + 'Variable/',
          data: {
            name: this.name,
            type: this.type
          },
          auth: {
            username: 'admin',
            password: 'After7'
          }
        })
          .then(response => {
            let newVariable = {
              id: response.data.id,
              Variable: this.Variable,
              type: this.type
            };
            this.Variable.push(newVariable);
            this.name = 'name';
            this.type = 'string';
          })
          .catch(error => {
            console.log(error);
          });
      }
    },
    setStatus(Variable_id, type) {
      const Variable = this.variable.filter(
        variable => variable_id.id === variable_id
      )[0];
      const name = Variable.name;
      axios({
        method: 'put',
        url: API_URL + 'Variable/' + Variable_id + '/',
        headers: {
          'Content-Type': 'application/json'
        },
        data: {
          type: type,
          name: name
        },
        auth: {
          username: 'admin',
          password: 'After7'
        }
      }).then(() => {
        Variable.type = type;
      });
    }
  }
};
</script>

<style lang="scss">
.select,
select {
  width: 100%;
}
.card {
  margin-bottom: 20px;
}
.done {
  opacity: 0.3;
}
</style>
