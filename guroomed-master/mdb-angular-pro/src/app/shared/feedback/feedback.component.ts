import { Component, OnInit } from '@angular/core';
import { NavbarService } from '../navbarService/navbar.service';

@Component({
  selector: 'app-feedback',
  templateUrl: './feedback.component.html',
  styleUrls: ['./feedback.component.scss']
})
export class FeedbackComponent implements OnInit {

  constructor(private nav: NavbarService) { }

  ngOnInit() {
    this.nav.show();
  }

  onClick(e) {
    console.log(e);
  }
}
