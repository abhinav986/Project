import { Component, OnInit } from '@angular/core';
import { HomeDataService } from 'app/home/home-data.service';
import { NavbarService } from 'app/shared/navbarService/navbar.service';
import { LoaderService } from 'app/shared/loader/loader.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent implements OnInit {
  newName = '';
  errorMessage: string;
  names: any[] = [];
  homeData: any[] = [];

  constructor(private homeDataService: HomeDataService, private nav: NavbarService, private loader: LoaderService) {
   }

  ngOnInit() {
    this.nav.show();
    this.loader.show();
    this.getHomeData();
  }

  getHomeData() {
    this.homeDataService.get()
      .subscribe(homeData => {
        this.homeData = homeData;
        this.loader.hide();
      },
      error => this.errorMessage = <any>error
      );
  }
}
