import "./Table.css";

const Table = ({ rows }) => {
  return (
    <table className="table">
      <tbody>
        {rows.map(row => (
          <tr className="table__row">
            <td className="table__cell">{row.rowId}</td>
            <td className="table__cell">{row.value}</td>
          </tr>))}
      </tbody>
    </table>
  );
}

export default Table;