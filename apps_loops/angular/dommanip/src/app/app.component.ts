import { Component } from '@angular/core';
import { Row } from 'src/types/row';
@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  status = "Ready to start";
  rowCount = 0;
  renderRows: Array<Row> = [];
  shouldRenderRows = false;

  inputChange(event: any): void {
    this.rowCount = event.target.value;
  }

  generate(): void {
    const rows: Array<Row> = [];
    for(let i = 1; i <= this.rowCount; i++) {
      rows.push({ rowId: i, value: i });
    }
    this.renderRows = rows;
    this.status = "Ready to render";
  }

  render(): void {
    this.shouldRenderRows = true;
    this.status = "Ready to update";
  }

  update(): void {
    this.renderRows = this.renderRows.map((row, i) => i % 2 === 0 ? ({ rowId: row.rowId, value: row.value * 2 }) : row)
    this.status = "Ready to remove";
  }

  remove(): void {
    this.renderRows = this.renderRows.filter((row, i) => i % 2 !== 0);
    this.status = "Finished";
  }

}
