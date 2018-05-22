import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { CompleterData, CompleterItem } from 'app/typescripts/pro/autocomplete';
import { CompleterService } from 'app/typescripts/pro';
import { ElasticService } from 'app/shared/elastic-search/elastic.service';

@Component({
  selector: 'app-elastic-search',
  templateUrl: './elastic-search.component.html',
  styleUrls: ['./elastic-search.component.scss']
})
export class ElasticSearchComponent implements OnInit {
  searchString: string;
  data: any[];
  searchData: any[];
  protected searchStr: string;
  protected dataService: CompleterData;

  constructor(private completerService: CompleterService, private router: Router, private elasticService: ElasticService) {
  }

  ngOnInit() {
  }

  // AutoSuggest function
  onKey(event) {
    this.elasticService.autoSuggestUrlData(event.target.value)
      .subscribe(searchData => {
        this.searchData = JSON.parse(searchData._body).searchData;
        this.dataService = this.completerService.local(this.searchData, 'id', 'id');
      });
  }

  // Get Data based on string
  getSearchString(selected: CompleterItem) {
    if (selected) {
      this.searchString = (typeof selected === 'string' ? selected : selected.originalObject.id);
      this.router.navigate(['/courses', this.searchString]);
      // this.router.navigate(['/courses'],{
      //   relativeTo: this._route,
      //   queryParams:  {
      //     search: this.searchString
      //   }
      // });
    }
  }
}
