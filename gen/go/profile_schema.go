// This file was generated from JSON Schema using quicktype, do not modify it directly.
// To parse and unparse this JSON data, add this code to your project and do:
//
//    profileSchema, err := UnmarshalProfileSchema(bytes)
//    bytes, err = profileSchema.Marshal()

package main

import "bytes"
import "errors"
import "encoding/json"

func UnmarshalProfileSchema(data []byte) (ProfileSchema, error) {
	var r ProfileSchema
	err := json.Unmarshal(data, &r)
	return r, err
}

func (r *ProfileSchema) Marshal() ([]byte, error) {
	return json.Marshal(r)
}

// The schema for how dbt plugins describe the profile configuration
type ProfileSchema struct {
	DbtMeta  Dbt              `json:"dbtMeta"`
	Profiles []ProfileElement `json:"profiles"`
}

type Dbt struct {
	ProfileVersion          string   `json:"profileVersion"`
	SuportedPackageVersions []string `json:"suportedPackageVersions,omitempty"`
}

type ProfileElement struct {
	DisplayName   *string               `json:"displayName,omitempty"`
	ID            *string               `json:"id,omitempty"`
	ProfileFields []ProfileFieldElement `json:"profileFields"`
}

type ProfileFieldElement struct {
	Description  *string       `json:"description,omitempty"`
	DisplayName  *string       `json:"displayName,omitempty"`
	FieldDefault *FieldDefault `json:"fieldDefault"`
	FieldType    FieldType     `json:"fieldType"`
	Sensitive    *bool         `json:"sensitive,omitempty"`
}

type FieldType string
const (
	Boolean FieldType = "boolean"
	Integer FieldType = "integer"
	String FieldType = "string"
)

type FieldDefault struct {
	Bool    *bool
	Integer *int64
	String  *string
}

func (x *FieldDefault) UnmarshalJSON(data []byte) error {
	object, err := unmarshalUnion(data, &x.Integer, nil, &x.Bool, &x.String, false, nil, false, nil, false, nil, false, nil, false)
	if err != nil {
		return err
	}
	if object {
	}
	return nil
}

func (x *FieldDefault) MarshalJSON() ([]byte, error) {
	return marshalUnion(x.Integer, nil, x.Bool, x.String, false, nil, false, nil, false, nil, false, nil, false)
}

func unmarshalUnion(data []byte, pi **int64, pf **float64, pb **bool, ps **string, haveArray bool, pa interface{}, haveObject bool, pc interface{}, haveMap bool, pm interface{}, haveEnum bool, pe interface{}, nullable bool) (bool, error) {
	if pi != nil {
		*pi = nil
	}
	if pf != nil {
		*pf = nil
	}
	if pb != nil {
		*pb = nil
	}
	if ps != nil {
		*ps = nil
	}

	dec := json.NewDecoder(bytes.NewReader(data))
	dec.UseNumber()
	tok, err := dec.Token()
	if err != nil {
		return false, err
	}

	switch v := tok.(type) {
	case json.Number:
		if pi != nil {
			i, err := v.Int64()
			if err == nil {
				*pi = &i
				return false, nil
			}
		}
		if pf != nil {
			f, err := v.Float64()
			if err == nil {
				*pf = &f
				return false, nil
			}
			return false, errors.New("Unparsable number")
		}
		return false, errors.New("Union does not contain number")
	case float64:
		return false, errors.New("Decoder should not return float64")
	case bool:
		if pb != nil {
			*pb = &v
			return false, nil
		}
		return false, errors.New("Union does not contain bool")
	case string:
		if haveEnum {
			return false, json.Unmarshal(data, pe)
		}
		if ps != nil {
			*ps = &v
			return false, nil
		}
		return false, errors.New("Union does not contain string")
	case nil:
		if nullable {
			return false, nil
		}
		return false, errors.New("Union does not contain null")
	case json.Delim:
		if v == '{' {
			if haveObject {
				return true, json.Unmarshal(data, pc)
			}
			if haveMap {
				return false, json.Unmarshal(data, pm)
			}
			return false, errors.New("Union does not contain object")
		}
		if v == '[' {
			if haveArray {
				return false, json.Unmarshal(data, pa)
			}
			return false, errors.New("Union does not contain array")
		}
		return false, errors.New("Cannot handle delimiter")
	}
	return false, errors.New("Cannot unmarshal union")

}

func marshalUnion(pi *int64, pf *float64, pb *bool, ps *string, haveArray bool, pa interface{}, haveObject bool, pc interface{}, haveMap bool, pm interface{}, haveEnum bool, pe interface{}, nullable bool) ([]byte, error) {
	if pi != nil {
		return json.Marshal(*pi)
	}
	if pf != nil {
		return json.Marshal(*pf)
	}
	if pb != nil {
		return json.Marshal(*pb)
	}
	if ps != nil {
		return json.Marshal(*ps)
	}
	if haveArray {
		return json.Marshal(pa)
	}
	if haveObject {
		return json.Marshal(pc)
	}
	if haveMap {
		return json.Marshal(pm)
	}
	if haveEnum {
		return json.Marshal(pe)
	}
	if nullable {
		return json.Marshal(nil)
	}
	return nil, errors.New("Union must not be null")
}
