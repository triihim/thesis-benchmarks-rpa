<template>
  <table class="table">
    <tbody>
      <tr class="table__row" v-for="row in rows" :key="row.rowId">
        <td class="table__cell">{{ row.rowId }}</td>
        <td class="table__cell">{{ row.value }}</td>
      </tr>
    </tbody>
  </table>
</template>

<script>
  export default {
    props: ["rows"]
  }
</script>

<style>
  .table {
    border-collapse: collapse;
    border: 1px solid #ccc;
    margin: 10px 0;
    width: 100%;
  }

  .table__row:nth-child(odd) {
    background-color: #eee;
  }

  .table__row:nth-child(even) {
    background-color: #ddd;
  }

  .table__cell {
    padding: 10px;
    text-align: center;
  }
</style>