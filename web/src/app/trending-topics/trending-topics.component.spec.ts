import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { TrendingTopicsComponent } from './trending-topics.component';

describe('TrendingTopicsComponent', () => {
  let component: TrendingTopicsComponent;
  let fixture: ComponentFixture<TrendingTopicsComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ TrendingTopicsComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(TrendingTopicsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
