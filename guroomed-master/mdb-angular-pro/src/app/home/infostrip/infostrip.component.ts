import { Component, OnInit, Input } from '@angular/core';

@Component({
  selector: 'app-infostrip',
  templateUrl: './infostrip.component.html',
  styleUrls: ['./infostrip.component.scss']
})
export class InfostripComponent implements OnInit {
  private _data: any;
  @Input()

  set data(data: any) {
    this._data = (data) || [];
  }

  get data(): any {
    return this._data;
  }
  constructor() { }

  ngOnInit() {
  }

}
