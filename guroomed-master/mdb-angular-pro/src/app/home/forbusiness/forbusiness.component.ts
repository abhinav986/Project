import { Component, OnInit, Input } from '@angular/core';

@Component({
  selector: 'app-forbusiness',
  templateUrl: './forbusiness.component.html',
  styleUrls: ['./forbusiness.component.scss']
})
export class ForbusinessComponent implements OnInit {
  _data:any;
  @Input()
  set data(data:any) {
    this._data = (data) || {name:"peace"};
  }
  get data(): any { return this._data; }

  constructor() { }

  ngOnInit() {
  }

}