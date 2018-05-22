import { Component, OnInit, Output, EventEmitter } from '@angular/core';
import { NavbarService } from 'app/shared/navbarService/navbar.service';

@Component({
  selector: 'app-course-search',
  templateUrl: './course-search.component.html',
  styleUrls: ['./course-search.component.scss']
})
export class CourseSearchComponent implements OnInit {
  selectedValue = 'Default';
  searchStringMessage: string;

  difficulty_level = '';
  languages = '';
  price = '';
  features = '';
  sortedBy = '';
  searchedData: any[] = [];
  queryParams: any = {};

  @Output() filterCheckBox: EventEmitter<any> = new EventEmitter();
  checkBoxFunc(element) {
    this.filterCheckBox.emit(element);
    if (element.value === undefined) {
      this.selectedValue = element.target.innerText;
    }
  }

  constructor(private nav: NavbarService) { }

  ngOnInit() {
    this.nav.show();
  }

}
