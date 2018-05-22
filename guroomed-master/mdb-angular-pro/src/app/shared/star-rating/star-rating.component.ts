import { Component, OnChanges, Input } from '@angular/core';

@Component({
  selector: 'app-star-rating',
  templateUrl: './star-rating.component.html',
  styleUrls: ['./star-rating.component.scss']
})
export class StarRatingComponent implements OnChanges {
  @Input() rating: number;
  starWidth: number;
  constructor() { }

  ngOnChanges(): void {
    this.starWidth = this.rating/5 * 100;
  } 

}
