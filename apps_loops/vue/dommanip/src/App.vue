<template>
  <main>
    <p id="status">{{status}}</p>
    <input id="inputRowCount" type="number" v-model="rowCount" />
    <button id="btnGenerate" @click="generate">Generate</button>
    <button id="btnRender" @click="render">Render</button>
    <button id="btnUpdate" @click="update">Update</button>
    <button id="btnRemove" @click="remove">Remove</button>
    <AppTable v-if="shouldRenderRows" :rows="renderRows"></AppTable>
  </main>
</template>

<script>
import AppTable from "./components/AppTable.vue";
export default {
  data() {
    return {
      status: "Ready to start",
      rowCount: 0,
      renderRows: [],
      shouldRenderRows: false,
    }
  },
  methods: {
    generate() {
      const rows = [];
      for(let i = 1; i <= this.rowCount; i++) {
        rows.push({ rowId: i, value: i });
      }
      this.renderRows = rows;
      this.status = "Ready to render";
    },
    render() {
      this.shouldRenderRows = true;
      this.status = "Ready to update";
    },
    update() {
      this.renderRows = this.renderRows.map((row, i) => i % 2 === 0 ? ({ rowId: row.rowId, value: row.value * 2 }) : row);
      this.status = "Ready to remove";
    },
    remove() {
      this.renderRows = this.renderRows.filter((row, i) => i % 2 !== 0);
      this.status = "Finished";
    }
  },  
  components: {
    AppTable
  }
}
</script>

<style>
  main {
    font-family: 'Courier New', Courier, monospace;
    margin: auto;
    border-radius: 10px;
    border: 2px solid black;
    padding: 20px;
    max-width: 500px;
    display: flex;
    flex-direction: column;
    text-align: center;
  }

  main button, main input {
    padding: 10px;
  }
</style>
