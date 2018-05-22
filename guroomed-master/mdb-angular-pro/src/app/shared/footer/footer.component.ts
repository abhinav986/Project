import { Component, OnInit } from '@angular/core';
import { NavbarService } from 'app/shared/navbarService/navbar.service';

@Component({
  selector: 'app-footer',
  templateUrl: './footer.component.html',
  styleUrls: ['./footer.component.scss']
})
export class FooterComponent implements OnInit {

  constructor(public nav: NavbarService) { }

  ngOnInit() {
  }

}
