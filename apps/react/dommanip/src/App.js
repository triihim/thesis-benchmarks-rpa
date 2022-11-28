import { useState } from "react";
import Table from "./Table";
import "./App.css";

const App = () => {
  const [status, setStatus] = useState("Ready to start");
  const [rowCount, setRowCount] = useState(0);
  const [renderRows, setRenderRows] = useState([]);
  const [shouldRenderRows, setShouldRenderRows] = useState(false);

  const generate = () => {
    const rows = [];
    for(let i = 1; i <= rowCount; i++) {
      rows.push({ rowId: i, value: i });
    }
    setRenderRows(rows);
    setStatus("Ready to render")
  }

  const render = () => {
    setShouldRenderRows(true);
    setStatus("Ready to update");
  }

  const update = () => {
    setRenderRows(prev => prev.map((row, i) => i % 2 === 0 ? ({ rowId: row.rowId, value: row.value * 2 }) : row));
    setStatus("Ready to remove");
  }

  const remove = () => {
    setRenderRows(prev => prev.filter((row, i) => i % 2 !== 0));
    setStatus("Finished");
  }

  return (
    <main>
      <p id="status">{status}</p>
      <input id="inputRowCount" type="number" onChange={(e) => setRowCount(e.target.value)} />
      <button id="btnGenerate" onClick={generate}>Generate</button>
      <button id="btnRender" onClick={render}>Render</button>
      <button id="btnUpdate" onClick={update}>Update</button>
      <button id="btnRemove" onClick={remove}>Remove</button>
      {shouldRenderRows && <Table rows={renderRows} />}
    </main>
  )
}

export default App;
