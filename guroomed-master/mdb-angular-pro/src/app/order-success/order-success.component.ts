import { Component, OnInit } from '@angular/core';
import { NavbarService } from '../shared/navbarService/navbar.service';
import { ActivatedRoute } from '@angular/router';
import { CourseDetailService } from '../services/coursedetail/course-detail.service';

@Component({
  selector: 'app-order-success',
  templateUrl: './order-success.component.html',
  styleUrls: ['./order-success.component.scss']
})
export class OrderSuccessComponent implements OnInit {

  total_price: any;
  tax_price: any;
  discount_price: any;
  course_price: any;
  orderedData = [];
  course_id: any;
  constructor(private nav: NavbarService, private route: ActivatedRoute, private courseDetails: CourseDetailService, ) { }

  ngOnInit() {
    this.nav.show();
    this.course_id = this.route.snapshot.queryParams['course_id[]'];
    this.course_price = this.route.snapshot.queryParams.course_price;
    this.discount_price = this.route.snapshot.queryParams.discount_price;
    this.tax_price = this.route.snapshot.queryParams.tax_price;
    this.total_price = this.route.snapshot.queryParams.total_price;
    if (Array.isArray(this.course_id)) {
      this.course_id.forEach(id => {
        this.courseDetails.get(id)
          .subscribe(data => {
            var order = data;
            this.orderedData.push(order)
          });
      });
    } else {
      this.courseDetails.get(this.course_id)
        .subscribe(data => {
          var order = data;
          this.orderedData.push(order);
        });
    }
  }

}
