import Stops from './Stops.js';
import Search from './Search.js';
import Census from './Census.js';
import StopSearch from './StopSearch.js';
import LikelihoodOfSearch from './LikelihoodOfSearch.js';
import UseOfForce from './UseOfForce.js';
import ContrabandHitRate from './ContrabandHitRate.js';
import RaceToggle from './RaceToggle.js';

if (typeof window.NC === 'undefined') {
  window.NC = {};
}

Object.assign(
  window.NC,

  Stops,
  Search,
  Census,
  StopSearch,
  LikelihoodOfSearch,
  UseOfForce,
  ContrabandHitRate,
  RaceToggle
);
