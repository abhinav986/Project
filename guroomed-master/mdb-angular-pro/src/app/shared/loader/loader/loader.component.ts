import { Component, OnInit } from '@angular/core';
import { LoaderService } from 'app/shared/loader/loader.service';

@Component({
  selector: 'app-loader',
  templateUrl: './loader.component.html',
  styleUrls: ['./loader.component.scss']
})
export class LoaderComponent implements OnInit {

  constructor( public loader: LoaderService) { }

  ngOnInit() {
  }

}
