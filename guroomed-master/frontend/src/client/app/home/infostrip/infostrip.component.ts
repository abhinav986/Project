import { Component, OnInit,SimpleChanges,Input } from '@angular/core';

@Component({
  selector: 'app-infostrip',
  templateUrl: '../app/home/infostrip/infostrip.component.html',
  styleUrls: ['../app/home/infostrip/infostrip.component.css']
})
export class InfostripComponent implements OnInit {
  private _data:any;
   @Input()
  set data(data:any) {
    this._data = (data) || [];
  }
  get data(): any { return this._data; }
  constructor() { }


  ngOnInit() {

  }
}
