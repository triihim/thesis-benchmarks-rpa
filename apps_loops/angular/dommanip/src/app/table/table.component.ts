import { Component, Input } from '@angular/core';
import { Row } from 'src/types/row';

@Component({
  selector: 'app-table',
  templateUrl: './table.component.html',
  styleUrls: ['./table.component.css']
})
export class TableComponent {
  @Input() rows: Array<Row> = [];
}
