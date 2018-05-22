import { Component, OnInit } from '@angular/core';
import { CourseFilterService } from 'app/course-fliter/course-filter.service';
import { ActivatedRoute } from '@angular/router';
import { ElasticService } from 'app/shared/elastic-search/elastic.service';
import { NavbarService } from 'app/shared/navbarService/navbar.service';
import { LoaderService } from 'app/shared/loader/loader.service';

@Component({
  selector: 'app-course-fliter',
  templateUrl: './course-fliter.component.html',
  styleUrls: ['./course-fliter.component.scss']
})
export class CourseFliterComponent implements OnInit {
  noFilter: boolean;
  noDataFound = false;
  sort: any;
  searchStringMessage: string;
  searchString: string;
  errorMessage: string;
  searchedCourseData: any;
  searchedCourseDataList: any;
  languages = [];
  difficulty_level: string;

  constructor(
    private route: ActivatedRoute,
    private searchService: ElasticService,
    private courseFilter: CourseFilterService,
    private nav: NavbarService,
    private loader: LoaderService
  ) {
  }

  ngOnInit() {
    this.nav.show();
    this.loader.show();
    this.route.params.subscribe(params => {
      this.searchString = params['searchStr'];

      this.searchService.searchCourseData(this.searchString)
        .subscribe(searchResponse => {
          this.searchedCourseData = JSON.parse(searchResponse._body);
          this.searchedCourseDataList = this.searchedCourseData.phit;
          this.loader.hide();
          if (this.searchedCourseDataList.length === 0) {
            this.searchStringMessage = `Your search "${this.searchString}" did not match any courses`;
            this.noFilter = true;
          } else {
            this.searchStringMessage = `Search results for "${this.searchString}"`;
            this.noFilter = false;
          }
        },
        error => this.errorMessage = <any>error
        );
    });
  }

  filterCourse(event) {

    if (event.checked === true) {
      this.languages.push(event.value);
    } else if (event.checked === false) {
      this.languages.splice(this.languages.indexOf(event.value), 1);
    }

    if (event.value === undefined) {
      this.sort = event.target.name;
    }

    this.courseFilter.getCourseFilterData(this.searchString, this.languages, this.sort)
      .subscribe(searchResponse => {
        this.searchedCourseData = JSON.parse(searchResponse['_body']);
        this.searchedCourseDataList = this.searchedCourseData.phit;
        if (this.searchedCourseDataList.length === 0) {
          this.noDataFound = true;
        } else {
          this.noDataFound = false;
        }
      },
      error => this.errorMessage = <any>error
      );
  }
}
