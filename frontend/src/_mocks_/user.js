import { faker } from '@faker-js/faker';
import { sample } from 'lodash';
import axios from "axios";

// utils
import { mockImgAvatar } from '../utils/mockImages';

// ----------------------------------------------------------------------

const checkAuthenticated = () => async () => {
    let formNames = []
    const res = await axios
      .get(`${process.env.REACT_APP_API_URL}/forms/get/`)
      .then((res) => {
        for(var i = 0; i < res.data.length; i += 1){
            formNames.push(res.data[i].name)
        }
    });
    return formNames;
}; 

let x=checkAuthenticated()
const users = [...Array(24)].map((_, index) => ({
  id: faker.datatype.uuid(),
  avatarUrl: mockImgAvatar(index + 1),
  name: faker.name.findName(),
  company: faker.company.companyName(),
  isVerified: faker.datatype.boolean(),
  status: sample(['active', 'banned']),
  role: sample([
    'Leader',
    'Hr Manager',
    'UI Designer',
    'UX Designer',
    'UI/UX Designer',
    'Project Manager',
    'Backend Developer',
    'Full Stack Designer',
    'Front End Developer',
    'Full Stack Developer'
  ])
}));

export default users;