import React from "react";
import { useState } from "react";
import axios from "axios";
import { faker } from "@faker-js/faker";
// import { TextField } from "./TextField";
import { TextField } from "@mui/material";
import * as Yup from "yup";
import "../css/formtemplate.css";
import { styled } from "@mui/material/styles";
import { Stack } from "@mui/material";
import { Typography } from "@mui/material";
import { LoadingButton } from "@mui/lab";
import { useFormik, Form, FormikProvider, connect } from "formik";

const ContentStyle = styled("div")(({ theme }) => ({
  maxWidth: "93%",
  display: "flex",
  flexDirection: "column",
  justifyContent: "center",
}));

function getFormName(url) {
  let name = url.substr(25, url.length);
  let formName = "";
  let index = 0;
  while (index < name.length) {
    if (name[index] == "%") {
      index += 3;
      formName += " ";
      continue;
    }
    formName += name[index];
    index += 1;
  }
  return formName;
}

function createKey(background, fieldName) {
  let key = "";
  for (let index = 0; index < background.length; index++) {
    if (background[index] == " ") {
      key += "_";
    } else key += background[index];
  }
  key += "_";
  for (let index = 0; index < fieldName.length; index++) {
    if (fieldName[index] == " ") {
      key += "_";
    } else key += fieldName[index];
  }
  return key;
}

function createValidationSchema(fields) {
  let validationSchema = {};
  for (let index = 0; index < fields.length; index++) {
    validationSchema[fields[index].name] = Yup.string().required("Required");
  }
  return validationSchema;
}

const sendFormData = (data) => {
  if (localStorage.getItem("formInstID")) {
    const config = {
      headers: {
        "Content-Type": "application/json",
        Accept: "application/json",
      },
    };
    const body = JSON.stringify({
      data: data,
      instID: localStorage.getItem("formInstID"),
    });
    try {
      const res = axios
        .post(
          `${process.env.REACT_APP_API_URL}/forms/create_form_instance/`,
          body,
          config
        )
        .then((res) => {
          console.log(res.data);
        });
    } catch (err) {
      console.log(err);
    }
  }
};

const sendFormInst = (name) => {
  if (localStorage.getItem("access")) {
    const config = {
      headers: {
        "Content-Type": "application/json",
        Accept: "application/json",
      },
    };
    const body = JSON.stringify({
      form: name,
      userEmail: localStorage.getItem("email"),
    });
    try {
      const res = axios
        .post(
          `${process.env.REACT_APP_API_URL}/forms/create_form_instance/`,
          body,
          config
        )
        .then((res) => {
          console.log(res.data);
        });
    } catch (err) {
      console.log(err);
    }
  }
};

export default function FormTemplate() {
  let formName = getFormName(window.location.pathname);
  const config = {
    headers: {
      "Content-Type": "application/json",
      Accept: "application/json",
    },
  };
  const body = JSON.stringify({ name: formName });
  const [loadPage, setLoadPage] = useState(0);
  const [formFields, setFormFields] = useState([]);
  const [validate, setValidate] = useState(Yup.object().shape({}));
  const [initialValues, setInitialValues] = useState({});

  const res = axios
    .post(
      `${process.env.REACT_APP_API_URL}/forms/get_form_fields/`,
      body,
      config
    )
    .then((res) => {
      let formNames = [];
      const tempInitialValues = {};
      for (var i = 0; i < res.data.length; i += 1) {
        let nameOfField = createKey(
          res.data[i].background,
          res.data[i].fieldName
        );
        console.log(res.data);
        formNames.push([
          res.data[i].fieldName,
          res.data[i].background,
          res.data[i].fieldType,
          nameOfField,
        ]);
        tempInitialValues[nameOfField] = "";
      }
      const formField = [...Array(formNames.length)].map((_, index) => ({
        id: faker.datatype.uuid(),
        background: formNames[index][1],
        fieldName: formNames[index][0],
        fieldType: formNames[index][2],
        name: formNames[index][3],
      }));
      if (loadPage == 0) {
        setLoadPage(1);
        setFormFields(formField);
        let schemax = createValidationSchema(formField);
        setValidate(Yup.object().shape(schemax));
        setInitialValues(tempInitialValues);
        // console.log(tempInitialValues);
      }
    });

  const formik = useFormik({
    initialValues: initialValues,
    validationSchema: validate,
    onSubmit: (values) => {
      console.log(values);
      sendFormInst(formName);
    },
  });

  const { errors, touched, values, isSubmitting, handleSubmit, getFieldProps } =
    formik;

  return (
    <div className="container mt-3">
      <ContentStyle>
        <div>
          <Stack sx={{ mb: 5 }}>
            <Typography variant="h3" gutterBottom>
              LEAVE FORM
            </Typography>
            <Typography sx={{ color: "text.secondary", fontSize: "1.3rem" }}>
              Please fill out the details below carefully.
            </Typography>
          </Stack>
          <FormikProvider value={formik}>
            <Form autoComplete="off" noValidate onSubmit={handleSubmit}>
              <Stack spacing={3}>
                {formFields.map((field) => {
                  return (
                    <ContentStyle key={field.id}>
                      {field.background == "" ? (
                        <div></div>
                      ) : (
                        <Typography
                          sx={{
                            color: "text.dark",
                            fontSize: "1rem",
                            marginBottom: "15px",
                            marginLeft: "7px",
                          }}
                        >
                          {field.background}
                        </Typography>
                      )}
                      <TextField
                        label={field.fieldName}
                        background={field.background}
                        name={field.name}
                        type={field.fieldType === "DATE" ? "date" : "text"}
                        {...getFieldProps(field.name)}
                        error={Boolean(
                          touched[field.name] && errors[field.name]
                        )}
                        helperText={touched[field.name] && errors[field.name]}
                      />
                    </ContentStyle>
                  );
                })}
              </Stack>
              <Stack
                direction="row"
                alignItems="center"
                justifyContent="space-between"
                sx={{
                  my: 4,
                  width: "93%",
                  paddingLeft: "50px",
                  paddingRight: "50px",
                }}
              >
                <LoadingButton
                  size="large"
                  type="submit"
                  variant="contained"
                  loading={isSubmitting}
                >
                  Submit Request
                </LoadingButton>

                {/* <LoadingButton
                  size="large"
                  type="submit"
                  variant="contained"
                  loading={isSubmitting}
                >
                  Save as Draft
                </LoadingButton> */}
              </Stack>
            </Form>
          </FormikProvider>
        </div>
      </ContentStyle>
    </div>
  );
}
