import { Component, OnInit } from '@angular/core';
import { ManagementService } from '../management.service';

@Component({
  selector: 'app-reviewer-list',
  templateUrl: './reviewer-list.component.html',
  styleUrls: ['./reviewer-list.component.scss']
})
export class ReviewerListComponent implements OnInit {

  reviewerList: Array<any>;
  constructor(private managementService: ManagementService) { }

  ngOnInit() {
    this.getReviewerList();
  }

  getReviewerList() {
    this.managementService.getReviewerRecord().subscribe(list => {
      if(list['status'] == 1){
        this.reviewerList = list['reviewers'];
      }
    });
  }

}
