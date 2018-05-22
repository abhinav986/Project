import { Component, OnInit, SimpleChanges,Input } from '@angular/core';

@Component({
  selector: 'app-forbusiness',
  templateUrl: '../app/home/forbusiness/forbusiness.component.html',
  styleUrls: ['../app/home/forbusiness/forbusiness.component.css']
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
